import sys
from obspy.core import UTCDateTime
import importlib
sys.path.append('lib')
import FDSNtools
import wrappers
importlib.reload(wrappers)


SDS_TOP='/RAIDZ/DATA/SDS'
trace_ids = ['NZ.WIZ.10.HHZ', 'NZ.WSRZ.10.HHZ']
centerlat=-37.52
centerlon=177.1825
searchRadiusDeg=0.25
fdsnURL = "GEONET"
subnet = 'Whakaari'
SGRAM_TOP = '/RAIDZ/IceWeb'


startt = UTCDateTime(2019,1,1)
endt = UTCDateTime(2019,12,12)
inv = FDSNtools.get_inventory(fdsnURL, startt, endt, centerlat, centerlon, searchRadiusDeg, network='NZ', station='*', channel='HHZ')
#wrappers.FDSN_to_SDS_daily_wrapper(startt-3600, endt, SDS_TOP, trace_ids=trace_ids, \
#        fdsnURL=fdsnURL, overwrite=False, inv=inv)
wrappers.SDS_to_ICEWEB_wrapper(startt, endt, SDS_TOP, sampling_interval=60.0, sourcelat=centerlat, \
            sourcelon=centerlon, inv=inv, trace_ids=trace_ids, overwrite=False, verbose=True, sgrammins=10, \
                equal_scale=True, dbscale=True, clim=[1e-8, 1e-5], subnet=subnet, SGRAM_TOP=SGRAM_TOP, rsamStepSize=3600, taperSecs=600)
