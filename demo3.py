import os, sys
from obspy.core import UTCDateTime
sys.path.append('lib')
import FDSNtools
import wrappers

#import importlib
#importlib.reload(wrappers)


fdsnURL = "GEONET"
subnet = 'Whakaari'

# The following could be turned into a main wrapper function within wrappers.py
# Then the next step would be to manage datasource for Stream and Inventory objects
# Currently we can only handle Inventory objects from FDSN. Adding support for local StationXML, and for dataless SEED and SACpz is further work.
# For Stream objects, we should be able to handle FDSN, SDS, and perhaps eventually Antelope and Seisan.
configDict = wrappers.read_config()
generalDict = configDict['general']
subnetsDf = configDict['subnets']
traceidsDf = configDict['traceids']
placesDf = configDict['places']
subnet_rows_df = subnetsDf[subnetsDf['subnet']==subnet]
for index, row in subnet_rows_df.iterrows():
    if not row['done']:

        # startt and endt
        startt = UTCDateTime(row['startdate'])
        endt = UTCDateTime(row['enddate'])
        if startt: # backfill/archive mode
            if not endt: # get enddate = now
                endt = UTCDateTime(now)
        else:
            startt = UTCDateTime(now)
            endt = startt + 86400 # run for 24 hours in real-time mode
        print(startt, endt)

        # traceids
        matching_traceids_df = traceidsDf[traceidsDf['subnet']==subnet]
        trace_ids = matching_traceids_df['trace_id'].to_list()
        print(trace_ids)

        # coordinates
        matching_places_df = placesDf[placesDf['Place']==subnet]
        print(matching_places_df)      
        centerlat = float(matching_places_df['Lat'])
        centerlon = float(matching_places_df['Lon'])
        seismicityRadiusKm = float(matching_places_df['RadiusKm'])
        searchRadiusDeg = (seismicityRadiusKm * 2)/110.5

        # inventory - where to get this from? if downloading from FDSN, can just get when reading station waveform data SCAFFOLD
        inv = FDSNtools.get_inventory(fdsnURL, startt, endt, centerlat, centerlon, searchRadiusDeg, network='*', station='*', channel='*')

        wrappers.SDS_to_Stream_wrapper(
            startt, \
            endt, \
            generalDict['SDS_TOP'], \
            freqmin=float(generalDict['freqmin']), \
            freqmax=float(generalDict['freqmax']), \
            zerophase=False, \
            corners=2, \
            sampling_interval=float(generalDict['samplingInterval']), \
            sourcelat=centerlat, \
            sourcelon=centerlon, \
            inv=inv, \
            trace_ids=trace_ids, \
            overwrite=False, \
            verbose=True, \
            timeWindowMinutes=int(generalDict['timeWindowMinutes']),  \
            timeWindowOverlapMinutes=int(generalDict['timeWindowMinutes'])/10, \
            subnet=subnet, \
            dbpath=generalDict['DBPATH'], \
            SGRAM_TOP = generalDict['SGRAM_TOP'] \
         )
        
        # SCAFFOLD
        print('Done. Update iceweb_subnets.csv accordingly.')

