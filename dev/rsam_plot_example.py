import os, sys
module_path = os.path.join(os.getcwd(), 'lib')
#sys.path.append('../lib')
sys.path.append(module_path)
print(sys.path)
import RSAM
from obspy.core import UTCDateTime
startt = UTCDateTime("2019-06-01T00:00:00.000")
endt = UTCDateTime("2019-12-11T00:00:00.000")
SDS_TOP=os.path.join(os.getenv('HOME'), 'SDS')
rsamWI = RSAM.RSAMobj()
rsamWI.read(startt, endt, SDS_TOP, metric='mean', speed=1, corrected=True)
rsamWI.plot()