import os
from datetime import datetime, timedelta
from tandemsource import TandemSourceApi

pump_id = os.environ["PUMP_ID"]
minDate = datetime.now() - timedelta(days=1)
maxDate = datetime.now()

minDate = minDate.strftime("%m-%d-%Y")
maxDate = maxDate.strftime("%m-%d-%Y")

TandemSourceApi().load_event_data(pump_id, minDate, maxDate)

