import pandas as pd
import io
import boto3
from collections import defaultdict
import os
import json
from datetime import date
from transformations import daily_transformations

bucket = os.environ["S3_BUCKET"]  

def upload_to_s3(local_path, bucket, key):
    s3 = boto3.client("s3")
    s3.upload_file(local_path, bucket, key)


def group_by_id(data, id_field='name'):
    grouped = defaultdict(list)
    for row in data:
        grouped[row[id_field]].append(row)
    return grouped

def get_transformed_data(grouped_data):
   return daily_transformations(grouped_data)

def write_transformed_data(transformed_data):
    username = os.getenv("USERNAME")
    output_path = f'jobs/data/{username}'
    
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    os.makedirs(output_path)
    with open(os.path.join(output_path, "transformed_data.json"), "w") as f:
        json.dump(transformed_data, f, indent=2)


def write_grouped_parquet(grouped_data, output_dir='output_parquet'):
    os.makedirs(output_dir, exist_ok=True)
    for group_id, rows in grouped_data.items():
        df = pd.DataFrame(rows)
        filepath = os.path.join(output_dir, f"{group_id}.parquet")
        df.to_parquet(filepath, index=False)      


def write_grouped_parquet_to_s3(user_id, grouped_data, bucket, engine='pyarrow'):
    s3 = boto3.client('s3')
    for group_id, rows in grouped_data.items():
        df = pd.DataFrame(rows)
        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False, engine=engine)
        buffer.seek(0)
        key = f"{date.today()}/{user_id}/{group_id}.parquet"
       
        s3.upload_fileobj(buffer, bucket, key)

def serialize_events(events, output_path):
    with open(output_path, "w") as f:
        for e in events:
            record = {
                "source": e.source,
                "id": e.id,
                "timestampRaw": e.timestampRaw,
                "seqNum": e.seqNum,
                "raw": e.raw.hex()  # preserve as hex string
            }
            f.write(json.dumps(record) + "\n")


def load_parsed_events(data):
    grouped_data = group_by_id(data)
    return write_grouped_parquet_to_s3(grouped_data, bucket, prefix='', engine='pyarrow')

def load_unparsed_events(data, user_id):

    file_name = f"raw_events_{date.today()}.jsonl"
    serialize_events(data, file_name)
    upload_to_s3(file_name, bucket, f"{date.today()}/{user_id}/{file_name}")

def load_data(data):
    event_data = []
    unparsed_events = []
    for e in data:
        if isinstance (e, dict):
            event_data.append(e)
    else:
        unparsed_events.append(e)
    transformed_data = get_transformed_data(event_data)
    write_transformed_data(transformed_data)    
    load_unparsed_events(unparsed_events)
    load_parsed_events(event_data)