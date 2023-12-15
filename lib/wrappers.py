import os
import numpy as np
import matplotlib.pyplot as plt
import obspy
import SDS
import RSAM
import Spectrograms
import gc
import sqlite3
import pandas as pd
from IPython.display import clear_output

def order_traces_by_distance(st, r=[], assert_channel_order=False): 
    st2 = obspy.Stream()
    if not r:
        r = [tr.stats.distance for tr in st]
    if assert_channel_order: # modifies r to order channels by (HH)ZNE and then HD(F123) etc.
        for i, tr in enumerate(st):
            c1 = int(tr.stats.location)/1000000
            numbers = 'ZNEF0123456789'
            c2 = numbers.find(tr.stats.channel[2])/1000000000
            r[i] += c1 + c2
    indices = np.argsort(r)
    for i in indices:
        tr = st[i].copy()
        st2.append(tr)

    return st2

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))    

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"sqlite version: {sqlite3.version}")
    #except Error as e:
    except Exception as e:
        print(e)
    finally:
        return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_iceweb_db(dbpath):

    sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
                                        subnet text NOT NULL,
                                        startTime integer NOT NULL,
                                        endTime integer NOT NULL,
                                        datasource text,
                                        rsamDone integer DEFAULT False,
                                        drsDone integer DEFAULT False,
                                        sgramDone integer DEFAULT False,
                                        specParamsDone integer DEFAULT False,
                                        locked integer DEFAULT False,
                                        PRIMARY KEY (subnet, startTime, endTime)
                                    ); """


    # create a database connection
    conn = create_connection(dbpath)
    print(conn)

    # create tables
    if conn is not None:
        # create index table
        create_table(conn, sql_create_products_table)
    else:
        print("Error! cannot create the database connection.")
    return conn
# subnet, startTime, endTime, datasource, rsamDone, drsDone, sgramDone, specParamsDone, locked


def insert_products_row(conn, subnet, startTime, endTime):
    """
    Create a new row into the products table
    :param conn:
    :param row
    :return: did it work (True, False)
    """
    sql = ''' INSERT INTO products(subnet, startTime, endTime)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, (subnet, startTime, endTime) )
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False


def select_products_row(conn, subnet, startTime, endTime):
    """
    Query tasks by subnet, startTime
    :param conn: the Connection object
    :param subnet:
    :param startTime:
    :param endTime
    :return:

    Can use this to check if rsamDone, drsDone, sgramDone, etc.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE subnet=? AND startTime=? AND endTime=?", (subnet, startTime, endTime))

    rows = cur.fetchall()
    if len(rows)==1:
        print(rows[0])
        return rows[0] # a tuple
    elif len(rows)==0:
        return False


def update_products_row(conn, subnet, startTime, endTime, field='rsamDone', value=True):
    """
    Query tasks by subnet, startTime
    :param conn: the Connection object
    :param subnet:
    :param startTime:
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(f"UPDATE products set {field}=? WHERE subnet=? AND startTime=? AND endTime=?", (value, subnet, startTime, endTime))
        conn.commit()
        return True
    except:
        return False

def lock_row(conn, subnet, startTime, endTime, create=False):
    row = select_products_row(conn, subnet, startTime, endTime)
    picklebase = f"{subnet}_{startTime}_{endTime}"
    if row:
        locked = row[-2]
        if locked:
            print(f"{picklebase} already locked. Cannot get a lock")
            return False
        else:
            if update_products_row(conn, subnet, startTime, endTime, field='locked', value=True): 
            	print(f"Got a lock on {picklebase}")
            	return True
            else:
                print(f"Failed trying to lock {picklebase}")
                return False

    elif create: # row does not exist
        if insert_products_row(conn, subnet, startTime, endTime):
            print(f"Inserted new row for {picklebase}")
            if update_products_row(conn, subnet, startTime, endTime, field='locked', value=True): 
            	print(f"Got a lock on {picklebase}")
            	return True
            else:
                print(f"Failed trying to lock {picklebase}")
                return False
        else:
            print(f"Inserting {picklebase} failed")
            return False
    else:
        print(f"Cannot lock {picklebase} as it does not exist")
        return False


def unlock_row(conn, subnet, startTime, endTime):
    row = select_products_row(conn, subnet, startTime, endTime)
    picklebase = f"{subnet}_{startTime}_{endTime}"
    if row:
        locked = row[-1]
        if locked:
            if update_products_row(conn, subnet, startTime, endTime, field='locked', value=False):
                print(f"{picklebase} unlocked")
                return True
            else:
                print(f"Failed to unlock {picklebase}")
                return False
        else:
            print(f"{picklebase} was not locked")
            return False

    else: # row does not exist
        print(f"{picklebase} not in table. cannot unlock")
        return -1

def SDS_to_Stream_wrapper(startt, endt, SDS_TOP, freqmin=0.5, freqmax=None, \
        zerophase=False, corners=2, sampling_interval=60.0, sourcelat=None, \
        sourcelon=None, inv=None, trace_ids=None, overwrite=True, verbose=False, \
        timeWindowMinutes=10,  timeWindowOverlapMinutes=5, subnet='unknown', \
        dbpath='iceweb_sqlite3.db', SGRAM_TOP='.'):
    '''
    Load Stream from SDS archive, instrument-correct it, add distance metrics.
    
    For each timewindow, two Stream objects are created: a Stream containing a velocity seismogram, and a Stream containing a displacement seismogram. 
    Velocity seismogram is used for RSAM and spectrograms. Displacement seismogram is used for Reduced Displacement.

        Parameters:
            startt (UTCDateTime): An ObsPy UTCDateTime marking the start date/time of the data request.
            endt (UTCDateTime)  : An ObsPy UTCDateTime marking the end date/time of the data request.
            SDS_TOP (str)       : The path to the SDS directory structure.

        Optional Name-Value Parameters:
            trace_ids (List)    : A list of N.S.L.C strings. Default None. If given, only these trace ids will be read from SDS archive.
            inv (Inventory)     : An ObsPy Inventory object. Default None. 
            sourcelat (float)   : Decimal degrees latitude for assumed seismic point source. Default None.
            sourcelon (float)   : Decimal degrees longitude for assumed seismic point source. Default None.
            freqmin (float) : Bandpass minimum. Default 0.5 Hz.
            freqmax (float) : Bandpass maximum. Default None (highpass only)
            zerophase (bool) : If True, a two-way pass, acausal, zero-phase bandpass filter is applied to the data. Default False, which is a causal one-way filter.
            corners (int) : Filter is applied this many times. Default 2.
            sampling_interval (float) : bin size (in seconds) for binning data to compute RSAM.
            overwrite (bool) : If True, overwrite existing data in RSAM archive.
            verbose (bool) : If True, additional output is genereated for troubleshooting.
            timeWindowMinutes (int) : number of minutes for each file. Default: 10
            timeWindowOverlapMinutes (int) : number of extra minutes to load before tapering and filtering. Trimmed off at end of process. Default: 5
            subnet (str) : a label to use for this particular set of N.S.L.C.'s


    '''   
    if os.path.isfile(dbpath):
        conn = create_connection(dbpath)
    else:
        conn = create_iceweb_db(dbpath)
    taperSecs = timeWindowOverlapMinutes * 60
    startOfTimeWindow = startt
    while startOfTimeWindow < endt:
        endOfTimeWindow = startOfTimeWindow + timeWindowMinutes * 60
        startStr = startOfTimeWindow.isoformat()
        endStr = endOfTimeWindow.isoformat()

        row = select_products_row(conn, subnet, startStr, endStr)
        if row: # row exists - so file exists, or previously existed
            startOfTimeWindow = endOfTimeWindow
            continue # nothing to do
        print('\n')
        print(f"Time now: {obspy.UTCDateTime.now().isoformat()}")
        print(f"Processing {startOfTimeWindow}")
        
        # read from SDS
        thisSDSobj = SDS.SDSobj(SDS_TOP) 
        
        if inv: # with inventory CSAM, Drs, and spectrograms

            thisSDSobj.read(startOfTimeWindow-taperSecs, endOfTimeWindow+taperSecs, speed=2, trace_ids=trace_ids)
            st = thisSDSobj.stream

            InventoryTools.attach_station_coordinates_from_inventory(inv, st)
            InventoryTools.attach_distance_to_stream(st, sourcelat, sourcelon) 
            r = [tr.stats.distance for tr in st]
            if verbose:
                print(f"SDS Stream: {st}")
                print(f"Distances: {r}")
            st = order_traces_by_distance(st, r, assert_channel_order=True)
            print(st, [tr.stats.distance for tr in st])
            #VEL = order_traces_by_distance(VEL, r, assert_channel_order=True)

            pre_filt = [freqmin/1.2, freqmin, freqmax, freqmax*1.2]
            for seismogramType in ['VEL', 'DISP']:
                if verbose:
                    print(f"Correcting to {seismogramType} seismogram")
                cst = st.copy().select(channel="*H*").remove_response(output=seismogramType, inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)
                if verbose:
                    print(f"Trimming to 24-hour day from {startOfTimeWindow} to {endOfTimeWindow}")
                cst.trim(starttime=startOfTimeWindow, endtime=endOfTimeWindow)
                if lock_row(conn, subnet, startStr, endStr, create=True):
                    StreamToIcewebProducts(cst, seismogramType, conn, subnet, startStr, endStr, SGRAM_TOP=SGRAM_TOP) 
                    unlock_row(conn, subnet, startStr, endStr)
                del cst

            del st, r, pre_filt
        gc.collect()
        startOfTimeWindow = endOfTimeWindow
    conn.close()
    
def StreamToIcewebProducts(st, seismogramType, conn, subnet, startStr, endStr, verbose=False, rsamSamplingIntervalSeconds=60, RSAM_TOP='.', SGRAM_TOP='.', dbscale=True, equal_scale=True, clim=[1e-8,1e-5], fmin=0.5, fmax=18.0, overwrite=False):
    '''
    Process Stream into IceWeb products.

    '''

    print("\n")
    print(f"Time now: {obspy.UTCDateTime.now().isoformat()}")
    if not lock_row(conn, subnet, startStr, endStr):
        print('Skipping. Cannot lock row')
        return
        
    if isinstance(st, obspy.Stream) and len(st)>0 and st[0].stats.npts>1000:
        pass
    else:
        print(f"Not a valid Stream object: {st}")
        return

    startt = st[0].stats.starttime
    endt = st[0].stats.endtime
    row = select_products_row(conn, subnet, startStr, endStr)
    if row:
        (subnet, startStr, endStr, datasource, rsamDone, drsDone, sgramDone, specParamsDone, locked) = row
    else:
        raise Exception("No corresponding row found in products table. This should be impossible!")

    ####################################
    if seismogramType=='VEL': # SCAFFOLD: make work for pressure too?

        # compute & save instrument-corrected RSAM
        if not rsamDone:
            if verbose:
                print(f"Computing corrected RSAM")
            st_abs = obspy.Stream()
            st_noabs = obspy.Stream()
            for tr in st:
                if tr.stats.config['keepRaw']:
                    st_noabs.append(tr)
                else:
                    st_abs.append(tr)
            if len(st_abs)>0:
                #thisRSAMobj = IceWeb.RSAMobj(st=st_abs, sampling_interval=rsamSamplingIntervalSeconds, verbose=verbose,  units='m/s', absolute=True)
                #thisRSAMobj.write(RSAM_SDS_TOP) # write RSAM to an SDS-like structure
                # need to prepare this stream
                st_abs.detrend('linear')
                metricsObj = RSAM.RSAMmetrics(st=st_abs, sampling_interval=rsamSamplingIntervalSeconds, absolute=True, filter=True)
                metricsObj.write(RSAM_TOP = RSAM_TOP) # write RSAM to an SDS-like structure                
            if len(st_noabs)>0:
                # no filtering
                #thisRSAMobj = IceWeb.RSAMobj(st=st_noabs, sampling_interval=rsamSamplingIntervalSeconds, verbose=verbose,  units='m/s', absolute=False)
                #thisRSAMobj.write(RSAM_SDS_TOP) # write RSAM to an SDS-like structure    
                metricsObj = RSAM.RSAMmetrics(st=st_noabs, sampling_interval=rsamSamplingIntervalSeconds, absolute=False, filter=False)
                metricsObj.write(RSAM_TOP = RSAM_TOP) # write RSAM to an SDS-like structure                   
            if verbose:
                print(f"Saving corrected RSAM to SDS")
            #del thisRSAMobj
            del metricsObj
            update_products_row(conn, subnet, startStr, endStr, field='rsamDone', value=True)

        # Spectrogram
        if not sgramDone:
            st_sgram = obspy.Stream()
            for tr in st:
                if tr.stats.config['sgram']:
                    st_sgram.append(tr)
            if len(st_sgram)>0:
                sgramdir = os.path.join(SGRAM_TOP, st_sgram[0].stats.network, startt.strftime('%Y'), startt.strftime('%j'))
                sgrambase = '%s_%s.png' % (subnet, startt.strftime('%Y%m%d-%H%M'))
                sgramfile = os.path.join(sgramdir, sgrambase)
                if not os.path.isdir(sgramdir):
                    os.makedirs(sgramdir)
                if not os.path.isfile(sgramfile) or overwrite:
                    print(f"Output file: {sgramfile}")
                    spobj = Spectrograms.icewebSpectrogram(stream=st_sgram)
                    spobj.plot(outfile=sgramfile, dbscale=dbscale, title=sgramfile, equal_scale=equal_scale, clim=clim, fmin=fmin, fmax=fmax)
                    del spobj
                    update_products_row(conn, subnet, startStr, endStr, field='sgramDone', value=True)
                plt.close('all')
                del sgramdir, sgrambase, sgramfile

    ###########################################
    elif seismogramType=='DISP':
        if not drsDone:
            # compute/write reduced displacement
            if verbose:
                print(f"Computing DRS")
            thisDRSobj = IceWeb.ReducedDisplacementObj(st=st, sampling_interval=rsamSamplingIntervalSeconds, verbose=verbose, units='m' )
            if verbose:
                print(f"Writing DRS to SDS")
            thisDRSobj.write(RSAM_SDS_TOP) # write Drs to an SDS-like structure
            del thisDRSobj
            update_products_row(conn, subnet, startStr, endStr, field='drsDone', value=True)

    unlock_row(conn, subnet, startStr, endStr)
    gc.collect()


class datasourceObj():
    def __init__(self, dstype, url, SDS_TOP=None): # create a datasource connection
        self.dstype = dstype
        self.url = url
        self.connector = None

        if self.dstype.lower() == 'sds': # learn how to process kwargs
            self.connector = SDS.SDSobj(SDS_TOP, sds_type='D', format='MSEED')
        elif self.dstype.lower() == 'fdsn': # learn how to process kwargs
            self.connector = obspy.clients.fdsn.Client(base_url=url)

    def get_waveforms(self, startt, endt, trace_ids=None, speed=2, verbose=False, inv=None):
        st = obspy.Stream()
        if self.dstype.lower() == 'sds': # deliver an inv object to get responses attached to Traces
            self.connector.read(startt, endt, trace_ids=trace_ids, speed=speed, verbose=verbose)
            st = self.connector.stream
            if inv:
                st.attach_response(inv)      
        elif self.dstype.lower() == 'fdsn':
            for trace_id in trace_ids:
                network, station, location, chancode = trace_id.split('.')
                this_st = dstype.connector.get_waveforms(
                    network,
                    station,
                    location,
                    chancode,
                    starttime=startt,
                    endtime=endt,
                    attach_response=True
                )                
                this_st.merge(fill_value=0, method=1)
                st += this_st 
        return st # Stream object, hopefully with responses attached

    def get_inventory(self, startt, endt, centerlat, centerlon, searchRadiusDeg, SDS_TOP=None, network='*', station='*', channel='*'):
        inv = None
        if self.dstype.lower() == 'sds':
            filename = os.path.join(self.connector.topdir, 'metadata', f"{centerlat}_{centerlon}_{startt.strftime('%Y%m%d')}_{endt.strftime('%Y%m%d')}_{searchRadiusDeg}.sml")
            if os.path.isfile(filename):
                inv = obspy.core.inventory.read_inventory(filename)
            else: 
                print(f"{filename} does not exist") 
        elif self.dstype.lower() == 'fdsn':
            inv = self.connector.get_stations(
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
            if SDS_TOP:
                filename = os.path.join(SDS_TOP, 'metadata', f"{centerlat}_{centerlon}_{startt.strftime('%Y%m%d')}_{endt.strftime('%Y%m%d')}_{searchRadiusDeg}.sml")
                inv.write(filename, format='STATIONXML')                
        return inv

    def close(self):
        if self.connector:
            if self.dstype.lower() == 'sds': # close SDS connector is just to delete references to that SDSobj
                pass
            elif self.dstype.lower() == 'fdsn':
                self.connector.close()
        self.connector = False
        gc.collect()



def read_config(configdir='config', leader='iceweb', PRODUCTS_TOP=None):
    
    config = dict()
    for which in ['general', 'jobs', 'traceids', 'places']:
        config[which] = pd.read_csv(os.path.join(configdir, f"{leader}_{which}.config.csv"))

    if PRODUCTS_TOP:
        config['general']['PRODUCTS_TOP'] = PRODUCTS_TOP

    vars = dict()
    for index, row in config['general'].iterrows():
        vars[row['Variable']] = row['Value']
        
    for key in vars:
        if '$' in vars[key]: # where substitutions take place
            parts = vars[key].split('/')
            if len(parts)==1:
                vars[key] = vars[parts[0][1:]]
            else:
                vars[key] = vars[parts[0][1:]] + '/' + '/'.join(parts[1:])
                
    config['general']=vars
    return config



def run_iceweb_job(subnet, configdir='config', configname='iceweb', PRODUCTS_TOP=None):

    #######################
    # GENERAL CONFIGURATION
    #######################

    configDict = read_config(configdir=configdir, leader=configname, PRODUCTS_TOP=PRODUCTS_TOP)
    generalDict = configDict['general']
    jobsDf = configDict['jobs']
    traceidsDf = configDict['traceids']
    placesDf = configDict['places']

    #######################
    # SELECT MATCHING JOBS
    #######################
    
    job_rows_df = jobsDf[jobsDf['subnet']==subnet]
    
    
    for index, row in job_rows_df.iterrows():
        if row['done'] or row['hold']:
            continue               

        #######################
        # CONFIGURE JOB
        #######################
       
        # startt and endt     
        startt = obspy.UTCDateTime(row['startdate'])
        endt = obspy.UTCDateTime(row['enddate'])
        if startt: # backfill/archive mode
            if not endt: # get enddate = now
                endt = obspy.UTCDateTime(now)
        else:                 
            startt = obspy.UTCDateTime(now)
            endt = startt + 86400 # run for 24 hours in real-time mode
        print('Timewindow: ', startt, endt)

        # traceids
        matching_traceids_df = traceidsDf[traceidsDf['subnet']==subnet]
        trace_ids = matching_traceids_df['trace_id'].to_list()
        #print(trace_ids)

        # coordinates
        #print(placesDf)
        matching_places_df = placesDf[placesDf['Place']==subnet]
        centerlat = float(matching_places_df['Lat'].iloc[0])
        centerlon = float(matching_places_df['Lon'].iloc[0])
        seismicityRadiusKm = float(matching_places_df['RadiusKm'].iloc[0])
        searchRadiusDeg = (seismicityRadiusKm * 2)/110.5

        ########################
        # GET DATASOURCE AND INV
        #######################

        # open datasourceObj
        dsobj = datasourceObj(row['datasource'], row['url'], SDS_TOP = generalDict['SDS_TOP'])

        # inventory - where to get this from? if downloading from FDSN, can just get when reading station waveform data SCAFFOLD
        inv = dsobj.get_inventory(startt, endt, centerlat, centerlon, searchRadiusDeg)
        if not inv:
            # try to load calibration info instead?
            inv = matching_traceids_df
        
        ########################
        # RUN JOB
        #######################

        #return # SCAFFOLD. Want to check above part first. Only run when SDS archive built.

        # replace following with a generic datasource to Stream wrapper
        process_timewindows(
            startt, \
            endt, \
            dsobj, \
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
            SGRAM_TOP = generalDict['SGRAM_TOP'], \
            RSAM_TOP = generalDict['RSAM_TOP'] \
         )

        # SCAFFOLD
        print('Done. Update iceweb_jobs.csv accordingly.')

        dsobj.close()



def process_timewindows(startt, endt, dsobj, freqmin=0.5, freqmax=None, \
        zerophase=False, corners=2, sampling_interval=60.0, sourcelat=None, \
        sourcelon=None, inv=None, trace_ids=None, overwrite=True, verbose=False, \
        timeWindowMinutes=10,  timeWindowOverlapMinutes=5, subnet='unknown', \
        dbpath='iceweb_sqlite3.db', SGRAM_TOP='.', RSAM_TOP='.'):
    '''
    Load Stream from datasource, instrument-correct it, add distance metrics.

    For each timewindow, two Stream objects are created: a Stream containing a velocity seismogram, and a Stream containing a displacement seismogram.
    Velocity seismogram is used for RSAM and spectrograms. Displacement seismogram is used for Reduced Displacement.

        Parameters:
            startt (UTCDateTime): An ObsPy UTCDateTime marking the start date/time of the data request.
            endt (UTCDateTime)  : An ObsPy UTCDateTime marking the end date/time of the data request.
            dsobj (Datasource object) : A datasource object

        Optional Name-Value Parameters:
            trace_ids (List)    : A list of N.S.L.C strings. Default None. If given, only these trace ids will be read from SDS archive.
            inv (Inventory)     : An ObsPy Inventory object. Default None.
            sourcelat (float)   : Decimal degrees latitude for assumed seismic point source. Default None.
            sourcelon (float)   : Decimal degrees longitude for assumed seismic point source. Default None.
            freqmin (float) : Bandpass minimum. Default 0.5 Hz.
            freqmax (float) : Bandpass maximum. Default None (highpass only)
            zerophase (bool) : If True, a two-way pass, acausal, zero-phase bandpass filter is applied to the data. Default False, which is a causal one-way filter.
            corners (int) : Filter is applied this many times. Default 2.
            sampling_interval (float) : bin size (in seconds) for binning data to compute RSAM.
            overwrite (bool) : If True, overwrite existing data in RSAM archive.
            verbose (bool) : If True, additional output is genereated for troubleshooting.
            timeWindowMinutes (int) : number of minutes for each file. Default: 10
            timeWindowOverlapMinutes (int) : number of extra minutes to load before tapering and filtering. Trimmed off at end of process. Default: 5
            subnet (str) : a label to use for this particular set of N.S.L.C.'s


    '''
    if os.path.isfile(dbpath):
        conn = create_connection(dbpath)
    else:
        conn = create_iceweb_db(dbpath)
    taperSecs = timeWindowOverlapMinutes * 60
    startOfTimeWindow = startt
    while startOfTimeWindow < endt:
        endOfTimeWindow = startOfTimeWindow + timeWindowMinutes * 60
        startStr = startOfTimeWindow.isoformat()
        endStr = endOfTimeWindow.isoformat()

        row = select_products_row(conn, subnet, startStr, endStr)
        if row: # row exists - so file exists, or previously existed
            startOfTimeWindow = endOfTimeWindow
            continue # nothing to do
        print('\n')
        print(f"Time now: {obspy.UTCDateTime.now().isoformat()}")
        print(f"Processing {startOfTimeWindow}")

        if isinstance(inv, obspy.Inventory) or isinstance(inv, pd.DataFrame): # with inventory CSAM, Drs, and spectrograms

            st = dsobj.get_waveforms(startOfTimeWindow-taperSecs, endOfTimeWindow+taperSecs, trace_ids=trace_ids)
            if isinstance(inv, obspy.Inventory):
                InventoryTools.attach_station_coordinates_from_inventory(inv, st)
                InventoryTools.attach_distance_to_stream(st, sourcelat, sourcelon)

                r = [tr.stats.distance for tr in st]
                if verbose:
                    print(f"Stream: {st}")
                    print(f"Distances: {r}")
                st = order_traces_by_distance(st, r, assert_channel_order=True)
                print(st, [tr.stats.distance for tr in st])
 
                pre_filt = [freqmin/1.2, freqmin, freqmax, freqmax*1.2]
                for seismogramType in ['VEL', 'DISP']:
                    if verbose:
                        print(f"Correcting to {seismogramType} seismogram")
                    cst = st.copy().select(channel="*H*").remove_response(output=seismogramType, inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)
                    if verbose:
                        print(f"Trimming to 24-hour day from {startOfTimeWindow} to {endOfTimeWindow}")
                    cst.trim(starttime=startOfTimeWindow, endtime=endOfTimeWindow)
                    if lock_row(conn, subnet, startStr, endStr, create=True):
                        StreamToIcewebProducts(cst, seismogramType, conn, subnet, startStr, endStr, SGRAM_TOP=SGRAM_TOP)
                        unlock_row(conn, subnet, startStr, endStr)
                    del cst

                del st, r, pre_filt
            elif isinstance(inv, pd.DataFrame): # make this work for KSC with Well Log data to do RSAM
                for index, row in inv.iterrows():
                    for tr in st:
                        if row['trace_id'] == tr.id:
                            tr.data = tr.data / row['calib']
                            if tr.stats.channel[1]=='H':
                                tr.stats['units'] = 'm/s'
                            elif tr.stats.channel[1]=='D':
                                tr.stats['units'] = 'Pa'
                            tr.stats['config'] = obspy.core.util.attribdict.AttribDict({'maxPower':row['maxPower'], 'keepRaw':row['keepRaw'], 'sgram':row['sgram'],  'calib':row['calib']})

                if lock_row(conn, subnet, startStr, endStr, create=True):
                    StreamToIcewebProducts(st, 'VEL', conn, subnet, startStr, endStr, SGRAM_TOP=SGRAM_TOP, RSAM_TOP=RSAM_TOP)
                    unlock_row(conn, subnet, startStr, endStr)
                del st                    
        clear_output(wait=True)        
        gc.collect()
        startOfTimeWindow = endOfTimeWindow
    conn.close()



if __name__ == '__main__':
    pass

