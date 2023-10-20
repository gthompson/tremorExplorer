import os, sys
from obspy.core import UTCDateTime
sys.path.append('lib')
import FDSNtools
import wrappers
import SDS

#import importlib
#importlib.reload(wrappers)


subnet = 'KSC'

preconfigured=True

if not preconfigured:
    # PRE-CONFIGURE CONFIGURATION
    startt = UTCDateTime(2022,8,1)
    endt = UTCDateTime(2022,12,5)
    SDS_TOP=os.path.join(os.getenv('HOME'), 'Dropbox', 'DATA', 'SDS')

    # get list of trace_ids from SDS archive
    thisSDSobj = SDS.SDSobj(SDS_TOP)
    trace_ids = thisSDSobj._sds_get_nonempty_traceids(startt, endt)
    print(trace_ids)

    for id in trace_ids:
        keepRaw = True
        sgram = False
        if id[-1] in 'ZNEF123456789' and id[-2] in 'HD':
            keepRaw = False
            if id[-1] in 'ZF4' and id[-2] in 'HD':
                sgram = True
        print(f"{id},{subnet},None,{keepRaw},{sgram}")
        # These have been appended to trace_ids config csv


# how do we create an inventory for the KSC network?
    # there is nothing to do for the well stations. they are already calibrated.
    # for the seismic and infrasound stations, we need appropriate responses for:
        # Trillum + Centaur
        # InfraBSU + Centaur
        # Chaparral M25 + Centaur
    # The shortcut is if there is no inv, just to supply calibration information from counts 2 Pa, and counts to m/s.
        # calibration info should be in the trace_ids config. would be 1 for well channels.
        # no Drs calculation if no inv.
        # but can still do CSAM and spectrograms.
        # could potentially do reduced velocity, and reduced pressure.
        # maybe the whole idea of reduced displacement is silly, and just do reduced velocity instead? or as well as?
    # TO DO:
        # add other parameters, from metrics.py. but get traditional iceweb stuff working first.

# RUN JOB
# call the wrapper
wrappers.run_iceweb_job('KSC', configdir='config', configname='laptop' )

