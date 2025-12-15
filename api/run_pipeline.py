import os
from datetime import datetime, timedelta
from api.tandemsource import TandemSourceApi

pump_id = os.environ["PUMP_ID"]
minDate = datetime.now() - timedelta(days=1)
maxDate = datetime.now()

TandemSourceApi().pump_events(pump_id, minDate, maxDate)