######################################################################
##   Additional tools for ObsPy FDSN client                         ##
######################################################################
import os
import obspy.core
#import obspy.clients.fdsn
#from libseisGT import smart_merge

# Import using: import obspyGT.FDSNtools

#CACHE_DIR = os.path.join(os.getcwd(), 'cache')
CACHE_DIR = os.path.join('.', 'cache')

def _check_client_or_string(fdsnThing):
    from obspy.clients.fdsn import Client
    if isinstance(fdsnThing, Client):
        return fdsnThing
    if isinstance(fdsnThing, str):
        return Client(base_url=fdsnThing)
    
def _make_cache_dir(cachedir):
    if not os.path.isdir(cachedir):
        os.mkdir(cachedir)

def _get_stationXML_filename(startt, endt, centerlat, centerlon, searchRadiusDeg, cachedir=CACHE_DIR):
    _make_cache_dir(cachedir)
    return os.path.join(cachedir, '%s_%s_%.4f_%.4f_%.2f.SML' % (startt.strftime('%Y%m%d%H%M'),endt.strftime('%Y%m%d%H%M'),centerlat,centerlon,searchRadiusDeg))

def _get_MSEED_filename(startt, endt, trace_ids, cachedir=CACHE_DIR):
    _make_cache_dir(cachedir)
    return os.path.join(cachedir, '%s_%s_%s_%s.MSEED' % (startt.strftime('%Y%m%d%H%M'),endt.strftime('%Y%m%d%H%M'),trace_ids[0],trace_ids[-1]))


def get_inventory(fdsnClient, startt, endt, centerlat, centerlon, searchRadiusDeg, network='*', station='*', channel='*', overwrite=False, cache=False ):
    """ 
    Get inventory of stations/channels available. Cache locally using fixed filenam, if cache==True. Default is to download each time.
    """
    stationXmlFile = _get_stationXML_filename(startt, endt, centerlat, centerlon, searchRadiusDeg)

    if os.path.isfile(stationXmlFile) and not overwrite:
        # load inv from file
        inv = obspy.core.inventory.read_inventory(stationXmlFile)
    else:
        # load inv from Client & save it        
        print('Trying to load inventory from %s to %s' % (startt.strftime('%Y/%m/%d %H:%M'), endt.strftime('%Y/%m/%d %H:%M')))
        fdsnClient = _check_client_or_string(fdsnClient)
        try:
            inv = fdsnClient.get_stations(
                network = network,
                station = station,
                channel = channel,
                latitude = centerlat,
                longitude = centerlon,
                maxradius = searchRadiusDeg,
                starttime = startt,
                endtime = endt,
                level = 'response'
            )
        except Exception as e: 
            print(e)
            print('-  no inventory available')
            return None
        else:
            if cache:         
                # Save the inventory to a stationXML file
                inv.write(stationXmlFile, format='STATIONXML')
                print('inventory saved to %s' % stationXmlFile)
            
            return inv



def get_stream(fdsnClient, trace_ids, startt, endt, overwrite=False, cache=False):
    """ 
    Load waveform data for all trace ids for this time range. Cache locally using fixed filename, if cache==True. Default is to download each time.
    """
    import numpy as np
    mseedfile = _get_MSEED_filename(startt, endt, trace_ids)
    if os.path.isfile(mseedfile) and not overwrite:
        # load raw data from file
        st = obspy.core.read(mseedfile)
        
    else:
        # load raw data from FDSN client
        st = obspy.core.Stream()
        fdsnClient = _check_client_or_string(fdsnClient)
        for trace_id in trace_ids:
            network, station, location, chancode = trace_id.split('.')
            print("net=%s, station=%s, location=%s, chancode=%s" % (network, station, location, chancode))
            try:
                this_st = fdsnClient.get_waveforms(
                    network,
                    station,
                    location,
                    chancode,
                    starttime=startt,
                    endtime=endt,
                    attach_response=True
                )

            except:
                print("- No waveform data available for %s for this event %s" % (trace_id, mseedfile))
                this_st = obspy.core.Stream()
                
            else: #SCAFFOLD - Replace with smart merge?
                if this_st:
                    try:
                        this_st.merge(fill_value=0, method=1)
                        st += this_st 
                    except:
                        #this_st = smart_merge(this_st) 
                        fsamp = np.nanmean([tr2.stats.sampling_rate for tr2 in this_st])
                        for tr2 in this_st:
                            tr2.stats.sampling_rate = fsamp
                        this_st.merge(fill_value=0, method=1)

                #for tr0 in st0:
                #    st.append(tr0)
                #st.merge(method=1,fill_value=0)                             
    
        if not st:
            print("- No waveform data available for this event %s" % mseedfile)
        else:
            try:
                st.merge(fill_value=0, method=1) #SCAFFOLD - Replace with smart merge?
            except:
                #st = smart_merge(this_st)
                fsamp = np.nanmean([tr2.stats.sampling_rate for tr2 in this_st])
                for tr2 in st:
                    tr2.stats.sampling_rate = fsamp
                st.merge(fill_value=0, method=1)
            # Save raw waveform data to miniseed
            if cache:
                st.write(mseedfile, format="MSEED") # write RAW data
    
    return st

def FDSN_to_SDS_daily_wrapper(startt, endt, SDS_TOP, centerlat=None, centerlon=None, searchRadiusDeg=None, trace_ids=None, \
        fdsnURL="http://service.iris.edu", overwrite=True, inv=None):
    '''
    Download Stream from FDSN server and save to SDS format. Default is to overwrite each time.
    
    NSLC combinations to download either come from (1) trace_ids name-value pair, (2) inv name-value pair, (3) circular search parameters, in that order.

        Parameters:
            startt (UTCDateTime): An ObsPy UTCDateTime marking the start date/time of the data request.
            endt (UTCDateTime)  : An ObsPy UTCDateTime marking the end date/time of the data request.

            SDS_TOP (str)       : The path to the SDS directory structure.

        Optional Name-Value Parameters:
            trace_ids (List)    : A list of N.S.L.C strings. Default None. If given, this overrides other options.
            inv (Inventory)     : An ObsPy Inventory object. Default None. If given, trace_ids will be extracted from it, unless explicity given.
            centerlat (float)   : Decimal degrees latitude for circular station search. Default None.
            centerlon (float)   : Decimal degrees longitude for circular station search. Default None.
            searchRadiusDeg (float) : Decimal degrees radius for circular station search. Default None.
            fdsnURL (str) : URL corresponding to FDSN server. Default is "http://service.iris.edu".
            overwrite (bool) : If True, overwrite existing data in SDS archive.

        Returns: None. Instead an SDS volume is created/expanded.

    '''

    secsPerDay = 86400  
    while startt<endt:
        print(startt)
        endOfRsamTimeWindow = startt+secsPerDay 
        # read from SDS - if no data download from FDSN

        thisSDSobj = SDS.SDSobj(SDS_TOP) 
        
        if thisSDSobj.read(startt, endOfRsamTimeWindow, speed=2) or overwrite: # non-zero return value means no data in SDS so we will use FDSN
            # read from FDSN
            if not trace_ids:
                if inv: 
                    trace_ids = InventoryTools.inventory2traceid(inv)
                else:
                    inv = FDSNtools.get_inventory(fdsnURL, startt, endOfRsamTimeWindow, centerlat, centerlon, \
                                                        searchRadiusDeg, overwrite=overwrite ) # could add N S L C requirements too
                    if inv:
                        trace_ids = InventoryTools.inventory2traceid(inv)
            if trace_ids:
                st = FDSNtools.get_stream(fdsnURL, trace_ids, startt, endOfRsamTimeWindow, overwrite=overwrite)
                thisSDSobj.stream = st
                thisSDSobj.write(overwrite=overwrite) # save raw data to SDS
            else:
                print('SDS archive not written to.')

    

        startt+=secsPerDay # add 1 day 
