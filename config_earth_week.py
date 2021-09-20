from datetime import datetime
import predict_week as p
from backports.datetime_fromisoformat import MonkeyPatch
import config_earth
from datetime import timedelta

MonkeyPatch.patch_fromisoformat()     # Hacky solution for Python 3.6 to use ISO format Strings
timedelta(days=1)
start_time = config_earth.start_time # Simulation start time. The end time needs to be within the downloaded forecast

#exec(open("saveNETCDF.py").read())

p.predict(start_time)
start_time1 = start_time.replace(day=start_time.day+1)
p.predict(start_time1)

start_time2 = start_time.replace(day=start_time1.day+1)
p.predict(start_time2)

start_time3 = start_time.replace(day=start_time2.day+1)
p.predict(start_time3)

start_time4 = start_time.replace(day=start_time3.day+1)
p.predict(start_time4)

start_time5 = start_time.replace(day=start_time4.day+1)
p.predict(start_time5)

start_time6 = start_time.replace(day=start_time5.day+1)
p.predict(start_time6)
