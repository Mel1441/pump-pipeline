import os
from datetime import datetime, timedelta
from tandemsource import TandemSourceApi
from eventparser.generic import decode_raw_events


def run_manually(pump_id, minDate, maxDate):
    return TandemSourceApi().pump_events(pump_id, minDate, maxDate)