import os, sys
from obspy.core import UTCDateTime
import importlib
sys.path.append('lib')
import FDSNtools
import wrappers
importlib.reload(wrappers)


if sys.platform == 'linux':
    PRODUCTS_TOP = '/RAIDZ/IceWeb'
elif sys.platform == 'darwin':
    PRODUCTS_TOP = os.getenv('HOME')

SDS_TOP=os.path.join(PRODUCTS_TOP,'SDS')
if not os.path.isdir(SDS_TOP):
    os.makedirs(SDS_TOP)
SGRAM_TOP = os.path.join(PRODUCTS_TOP, 'sgram10min')
if not os.path.isdir(SGRAM_TOP):
    os.makedirs(SGRAM_TOP)
PICKLEDIR = os.path.join(PRODUCTS_TOP, 'PICKLEFILE_QUEUE')
if not os.path.isdir(PICKLEDIR):
    os.makedirs(PICKLEDIR)

trace_ids = ['NZ.WIZ.10.HHZ', 'NZ.WSRZ.10.HHZ']
centerlat=-37.52
centerlon=177.1825
searchRadiusDeg=0.25
fdsnURL = "GEONET"
subnet = 'Whakaari'
icewebdb = os.path.join(PRODUCTS_TOP, 'iceweb_sqlite3.db')
startt = UTCDateTime(2019,1,1)
endt = UTCDateTime(2019,12,12)
inv = FDSNtools.get_inventory(fdsnURL, startt, endt, centerlat, centerlon, searchRadiusDeg, network='NZ', station='*', channel='HHZ')
wrappers.picklefileGobblerToIceweb(PICKLEDIR, verbose=True, rsamSamplingIntervalSeconds=60, RSAM_SDS_TOP=SDS_TOP, SGRAM_TOP=SGRAM_TOP, dbscale=True, \
         equal_scale=True, clim=[1e-8,1e-5], fmin=0.5, fmax=20.0, overwrite=False, dbpath=icewebdb)

