from datetime import datetime
import subprocess
from backports.datetime_fromisoformat import MonkeyPatch

MonkeyPatch.patch_fromisoformat()  # Hacky solution for Python 3.6 to use ISO format Strings

#hw = 64
#hw = 24

hw = 24
gfs = "2021-09-23 06:00:00"  # Forecast start time, should match a downloaded forecast
start_time = datetime.fromisoformat("2021-09-23 13:30:00")  # Simulation start time. The end time needs to be within the downloaded forecast


balloon_properties = dict(
    shape='sphere',
    d=7,  # (m) Diameter of Sphere Balloon
    mp=3.5,  # (kg) Mass of Payload
    areaDensityEnv=939. * 7.87E-6,  # (Kg/m^2) rhoEnv*envThickness
    mEnv=1.75,  # (kg) Mass of Envelope - SHAB1
    cp=1250.,  # (J/(kg K)) Specific heat of envelope material
    absEnv=.6,  # Absorbiviy of envelope material
    emissEnv=.6,  # Emisivity of enevelope material
    Upsilon=2.5,  # Ascent Resistance coefficient
)

# These parameters are for both downloading new forecasts, and running simulations with downloaded forecasts.
netcdf = dict(
    nc_file=("forecasts/gfs_0p25_" + gfs[0:4] + gfs[5:7] + gfs[8:10] + "_" + gfs[11:13] + ".nc"),
    # file structure for downloading .25 resolution NOAA forecast data.
    nc_start=datetime.fromisoformat(gfs),  # Start time of the downloaded netCDF file
    hourstamp=gfs[11:13],  # parsed from gfs timestamp

    res=0.25,  # (deg) Do not change
    lat_range=40,  # (.25 deg)
    lon_range=40,  # (.25 deg)
    hours3=hw,  # (1-80) In intervals of 3 hours.  hour_index of 8 is 8*3=24 hours
    # hours3=60,  # (1-80) In intervals of 3 hours.  hour_index of 8 is 8*3=24 hours
)

simulation = dict(
    start_time=start_time,  # (UTC) Simulation Start Time, updated above
    sim_time=16,  # (hours) Simulation time in hours (for trapezoid.py)

    vent=0.0,  # (kg/s) Vent Mass Flow Rate  (Do not have an accurate model of the vent yet, this is innacurate)
    alt_sp=15000.0,  # (m) Altitude Setpoint
    v_sp=0.,  # (m/s) Altitude Setpoint, Not Implemented right now
    start_coord={
        # "lat": 35.811422,  # (deg) Latitude
        # "lon": -99.193882,  # (deg) Longitude
        # "alt": 561.,  # (m) Elevation
        "lat": 36.1626,  # (deg) Latitude
        "lon": -96.8358,  # (deg) Longitude
        "alt": 300.,  # (m) Elevation
        "timestamp": start_time,  # timestamp
    },
    min_alt=408.,  # starting altitude. Generally the same as initial coordinate
    float=11500.  # Maximum float altitude for simple trapezoidal trajectories
)

GFS = dict(
    GFSrate=60,  # (s) How often New Wind speeds are looked up
)

earth_properties = dict(
    Cp_air0=1003.8,  # (J/Kg*K)  Specifc Heat Capacity, Constant Pressure
    Cv_air0=716.,  # (J/Kg*K)  Specifc Heat Capacity, Constant Volume
    Rsp_air=287.058,  # (J/Kg*K) Gas Constant
    P0=101325.0,  # (Pa) Pressure @ Surface Level
    emissGround=.95,  # assumption
    albedo=0.17,  # assumption
)

dt = 2.0  # (s) Time Step for integrating (If error's occur, use a lower step size)

#exec(open("saveNETCDF.py").read())
