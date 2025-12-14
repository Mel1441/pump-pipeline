import struct
import base64

from dataclasses import dataclass

from .raw_event import RawEvent, EVENT_LEN
from .events import EVENT_IDS
from .utils import batched
import pandas as pd
from .event_schemas import base, event_schemas


def Event(x):
    raw_event = RawEvent.build(x)

    if not raw_event.id in EVENT_IDS:
        return raw_event
    return EVENT_IDS[raw_event.id].build(x).todict()
    #for e_id in EVENT_IDS:
     #   if raw_event.id == e_id:
      #      data = []
      #      row = EVENT_IDS[raw_event.id].build(x).todict()
      #      data.append(row)
      #      df = pd.DataFrame(data, columns=[base, event_schemas[e_id] ])
      #      print(df)
     

Events = lambda x: (Event(bytearray(e)) for e in batched(x, EVENT_LEN))

def decode_raw_events(raw):
    return base64.b64decode(raw)