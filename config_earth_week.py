from datetime import datetime
import predict_week as p
from backports.datetime_fromisoformat import MonkeyPatch

MonkeyPatch.patch_fromisoformat()     # Hacky solution for Python 3.6 to use ISO format Strings

start_time = datetime.fromisoformat("2021-09-15 13:30:00") # Simulation start time. The end time needs to be within the downloaded forecast

#exec(open("saveNETCDF.py").read())

p.predict(start_time)
start_time = datetime.fromisoformat("2021-09-16 13:30:00")
p.predict(start_time)

start_time = datetime.fromisoformat("2021-09-17 13:30:00")
p.predict(start_time)

start_time = datetime.fromisoformat("2021-09-18 13:30:00")
p.predict(start_time)

start_time = datetime.fromisoformat("2021-09-19 13:30:00")
p.predict(start_time)

start_time = datetime.fromisoformat("2021-09-20 13:30:00")
p.predict(start_time)
