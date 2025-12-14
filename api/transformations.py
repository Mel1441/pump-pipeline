import pandas as pd
import numpy as np

def get_df(data):
    df = pd.DataFrame(data)
    return df.drop_duplicates()

def sum_data(data, colName):
    df = get_df(data)
    return df[colName].sum()

def get_count(data, colName):
    df = get_df(data)
    return df.shape[0]

def get_max(data, colName):
    df = get_df(data)
    return df.max(axis=0)[colName]

def get_min(data, colName):
    df = get_df(data)
    return df.min(axis=0)[colName]

def get_basal_increase(data):
    df = get_df(data)
    total_count = df.shape[0]
    more_basal = np.where(df['commandedRate'] > df['profileBasalRate'])
    more_count = len(more_basal[0])
    increase_time = more_count / total_count
    return increase_time

def get_basal_decrease(data):
    df = get_df(data)
    total_count = df.shape[0]
    less_basal = np.where(df['commandedRate'] < df['profileBasalRate'])
    less_count = len(less_basal[0])
    decrease_time = less_count / total_count
    return decrease_time

def daily_transformations(data):
    total_carbs = sum_data(data['carbs_entered'], 'carbs')
    max_bg = get_max(data["cgm_data_g7"], 'currentglucosedisplayvalue')
    min_bg = get_min(data["cgm_data_g7"], 'currentglucosedisplayvalue')
    count_carbs_entered = get_count(data['carbs_entered'], 'carbs')
    basal_increase = get_basal_increase(data['basal_delivery'])
    basal_decrease = get_basal_decrease(data['basal_delivery'])
    return dict(
        totalCarbs = total_carbs,
        maxBG = max_bg,
        minBG = min_bg,
        countCarbs = count_carbs_entered,
        basalIncrease = basal_increase,
        basalDecrease = basal_decrease
    )
