import os
import numpy as np
import matplotlib.pyplot as plt
from obspy.core import Stream, read
import SDS
import FDSNtools
import InventoryTools
import IceWeb
import gc

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



def SDS_to_RSAM_wrapper(startt, endt, SDS_TOP, freqmin=0.5, freqmax=15.0, \
        zerophase=False, corners=2, sampling_interval=60.0, sourcelat=None, \
            sourcelon=None, inv=None, trace_ids=None, overwrite=True, verbose=False):
    '''
    Load Stream from SDS archive and create RSAM metrics. RSAM by default is the mean absolute value in each 60-s window.
    
    Raw RSAM (counts) is generated by default. If inv name-value parameter given, an instrument corrected RSAM (m/s) will be generated.
    If sourcelat and sourcelon name-value parameters given, surface-wave reduced displacement (cm^2) will be generated.

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
            freqmax (float) : Bandpass maximum. Default 15.0 Hz.
            zerophase (bool) : If True, a two-way pass, acausal, zero-phase bandpass filter is applied to the data. Default False, which is a causal one-way filter.
            corners (int) : Filter is applied this many times. Default 2.
            sampling_interval (float) : bin size (in seconds) for binning data to compute RSAM.
            overwrite (bool) : If True, overwrite existing data in RSAM archive.

        Returns: None. Instead an RSAM volume (a variant of an SDS volume) is created/expanded.

    '''   

    secsPerDay = 86400  
    while startt<endt:
        print(startt)
        endOfRsamTimeWindow = startt+secsPerDay #-1/10000
        # read from SDS - if no data download from FDSN

        thisSDSobj = SDS.SDSobj(SDS_TOP) 
        if not thisSDSobj.read(startt-3600, endOfRsamTimeWindow+3600, speed=2, trace_ids=trace_ids) or overwrite: # non-zero return value means no data in SDS so we will use FDSN

            # compute instrument-corrected RSAM
            thisRSAMobj = RSAMobj(st=thisSDSobj.stream.copy(), inv=inv, sampling_interval=sampling_interval, \
                              freqmin=freqmin, zerophase=zerophase, corners=corners, verbose=verbose, startt=startt, endt=endOfRsamTimeWindow)
            thisRSAMobj.write(SDS_TOP) # write RSAM to an SDS-like structure
        
            # compute/write reduced displacement
            if sourcelat and sourcelon and inv:
                thisDRSobj = ReducedDisplacementObj(st=thisSDSobj.stream.copy(), inv=inv, sampling_interval=sampling_interval, \
                                freqmin=freqmin, freqmax=freqmax, zerophase=zerophase, corners=corners, \
                                     sourcelat=sourcelat, sourcelon=sourcelon, verbose=verbose, startt=startt, endt=endOfRsamTimeWindow )
                thisDRSobj.write(SDS_TOP) # write Drs to an SDS-like structure
    

        startt+=secsPerDay # add 1 day 


def SDS_to_spectrogram_wrapper(startt, endt, SDS_TOP, trace_ids, windowlength=600, overwrite=False, equal_scale=True, dbscale=True, clim=None, inv=None, verbose=False):
    '''
    Load Stream from SDS archive and create RSAM metrics. RSAM by default is the mean absolute value in each 60-s window.
    
    Raw RSAM (counts) is generated by default. If inv name-value parameter given, an instrument corrected RSAM (m/s) will be generated.
    If sourcelat and sourcelon name-value parameters given, surface-wave reduced displacement (cm^2) will be generated.

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
            freqmax (float) : Bandpass maximum. Default 15.0 Hz.
            zerophase (bool) : If True, a two-way pass, acausal, zero-phase bandpass filter is applied to the data. Default False, which is a causal one-way filter.
            corners (int) : Filter is applied this many times. Default 2.
            sampling_interval (float) : bin size (in seconds) for binning data to compute RSAM.
            overwrite (bool) : If True, overwrite existing data in RSAM archive.

        Returns: None. Instead an RSAM volume (a variant of an SDS volume) is created/expanded.

    '''   
    startOfSgramTimeWindow = startt
    freqmin=0.2
    freqmax=25.0
    while startOfSgramTimeWindow<endt:
        print(startOfSgramTimeWindow)
        endOfSgramTimeWindow = startOfSgramTimeWindow+windowlength #-1/10000
        # read from SDS - if no data download from FDSN

        thisSDSobj = SDS.SDSobj(SDS_TOP) 
        
        
        if inv:
            thisSDSobj.read(startOfSgramTimeWindow-windowlength/2, endOfSgramTimeWindow+windowlength/2, speed=2, trace_ids=trace_ids)
            st = thisSDSobj.stream
            pre_filt = [freqmin/1.2, freqmin, freqmax, freqmax*1.2]
            for tr in st:
                if tr.stats.channel[2] in 'ENZ' : # filter seismic channels only
                    print('Processing %s' % tr.id)
                    tr.remove_response(output='DISP', inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)    
            st.trim(starttime=startOfSgramTimeWindow, endtime=endOfSgramTimeWindow)
        else:
            thisSDSobj.read(startOfSgramTimeWindow, endOfSgramTimeWindow, speed=2, trace_ids=trace_ids)
            st = thisSDSobj.stream

        spobj = IceWeb.icewebSpectrogram(stream=st)
        sgramfile = '%s.%s.png' % (st[0].stats.network, startOfSgramTimeWindow.strftime('%Y%m%dT%H%M%S'))
        if not os.path.isfile(sgramfile) or overwrite:
            print(sgramfile)
            spobj.plot(outfile=sgramfile, dbscale=dbscale, title=sgramfile, equal_scale=equal_scale, clim=clim, fmin=freqmin, fmax=freqmax)

        startOfSgramTimeWindow+=windowlength

def order_traces_by_distance(st, r=[], assert_channel_order=False): 
    st2 = Stream()
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


def SDS_to_ICEWEB_wrapper(startt, endt, SDS_TOP, freqmin=0.5, freqmax=15.0, \
        zerophase=False, corners=2, sampling_interval=60.0, sourcelat=None, \
            sourcelon=None, inv=None, trace_ids=None, overwrite=True, verbose=False, sgrammins=10,  \
                equal_scale=True, dbscale=True, clim=[1e-8, 1e-5], subnet=None, SGRAM_TOP='.', rsamStepSize=86400, taperSecs=3600):
    '''
    Load Stream from SDS archive and create RSAM metrics. RSAM by default is the mean absolute value in each 60-s window.
    
    Raw RSAM (counts) is generated by default. If inv name-value parameter given, an instrument corrected RSAM (m/s) will be generated.
    If sourcelat and sourcelon name-value parameters given, surface-wave reduced displacement (cm^2) will be generated.

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
            freqmax (float) : Bandpass maximum. Default 15.0 Hz.
            zerophase (bool) : If True, a two-way pass, acausal, zero-phase bandpass filter is applied to the data. Default False, which is a causal one-way filter.
            corners (int) : Filter is applied this many times. Default 2.
            sampling_interval (float) : bin size (in seconds) for binning data to compute RSAM.
            overwrite (bool) : If True, overwrite existing data in RSAM archive.
            verbose (bool) : If True, additional output is genereated for troubleshooting.
            equal_scale (bool) : If True, all spectrograms will be scaled the same.
            dbscale (bool) : If True, a logarithmic scale will be used for spectrograms. If False, a linear scale, which has limited dynamic range.
            clim (tuple, 2 elements) : Lower and upper end (in m/s) of colormap used for spectrograms. Default: (1e-8, 1e-5)
            SGRAM_TOP (string) : Path to top directory for saving spectrograms.
            rsamStepSize (int) : step size in seconds of time window used for RSAM and DRS calculations. Default: 86400 (1 day). 
            taperSecs (int) : seconds of extra data to load for response removal tapering. Default: 3600 (1 hour)
            sgrammins (int) : number of minutes for each spectrogram. Default: 10

        Returns: None. Instead an RSAM volume (a variant of an SDS volume) is created/expanded.

    '''   
    
    startOfRsamTimeWindow = startt
    while startOfRsamTimeWindow < endt:
        f"Processing {startOfRsamTimeWindow}"
        endOfRsamTimeWindow = startOfRsamTimeWindow + rsamStepSize
        # read from SDS
        thisSDSobj = SDS.SDSobj(SDS_TOP) 
        
        if inv: # with inventory CSAM, Drs, and spectrograms

            thisSDSobj.read(startOfRsamTimeWindow-taperSecs, endOfRsamTimeWindow+taperSecs, speed=2, trace_ids=trace_ids)
            st = thisSDSobj.stream

            InventoryTools.attach_station_coordinates_from_inventory(inv, st)
            InventoryTools.attach_distance_to_stream(st, sourcelat, sourcelon) 
            r = [tr.stats.distance for tr in st]
            if verbose:
                f"SDS Stream: {st}"
                f"Distances: {r}"
            st = order_traces_by_distance(st, r, assert_channel_order=True)
            print(st, [tr.stats.distance for tr in st])
            #VEL = order_traces_by_distance(VEL, r, assert_channel_order=True)

            pre_filt = [freqmin/1.2, freqmin, freqmax, freqmax*1.2]
            if verbose:
                f"Correcting to velocity seismogram"
            VEL = st.copy().select(channel="*H*").remove_response(output='VEL', inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)
            if verbose:
                f"Correcting to displacement seismogram"
            DISP = st.copy().select(channel="*H*").remove_response(output='DISP', inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)
            if verbose:
                f"Trimming to 24-hour day from {startOfRsamTimeWindow} to {endOfRsamTimeWindow}"
            VEL.trim(starttime=startOfRsamTimeWindow, endtime=endOfRsamTimeWindow)
            DISP.trim(starttime=startOfRsamTimeWindow, endtime=endOfRsamTimeWindow)

            # compute instrument-corrected RSAM
            if verbose:
                f"Computing corrected RSAM"
            thisRSAMobj = IceWeb.RSAMobj(st=VEL, inv=inv, sampling_interval=sampling_interval, freqmin=freqmin, freqmax=freqmax, \
                               zerophase=zerophase, corners=corners, verbose=verbose, startt=startOfRsamTimeWindow, endt=endOfRsamTimeWindow, units='m/s', absolute=True)
            if verbose:
                f"Saving corrected RSAM to SDS"
            thisRSAMobj.write(SDS_TOP) # write RSAM to an SDS-like structure

            # compute/write reduced displacement
            if sourcelat and sourcelon:
                if verbose:
                    f"Computing DRS"
                thisDRSobj = IceWeb.ReducedDisplacementObj(st=DISP, inv=inv, sampling_interval=sampling_interval, \
                                freqmin=freqmin, freqmax=freqmax, zerophase=zerophase, corners=corners, \
                                     sourcelat=sourcelat, sourcelon=sourcelon, verbose=verbose, units='m' )
                if verbose:
                    f"Writing DRS to SDS"
                thisDRSobj.write(SDS_TOP) # write Drs to an SDS-like structure

            # spectrograms
            startOfSgramTimeWindow = startOfRsamTimeWindow
            while startOfSgramTimeWindow < endOfRsamTimeWindow:
                endOfSgramTimeWindow = startOfSgramTimeWindow + sgrammins * 60
                if verbose:
                    f"Generating spectrogram from {startOfSgramTimeWindow} to {endOfSgramTimeWindow}"
                tw_st = VEL.copy().trim(starttime=startOfSgramTimeWindow, endtime=endOfSgramTimeWindow)
                if isinstance(tw_st, Stream) and len(tw_st)>0 and tw_st[0].stats.npts>1000:
                    pass
                else:
                    if verbose:
                        f"- Not possible"
                    startOfSgramTimeWindow += sgrammins * 60    
                    continue
                sgramdir = os.path.join(SGRAM_TOP, tw_st[0].stats.network, startOfSgramTimeWindow.strftime('%Y'), startOfSgramTimeWindow.strftime('%j'))
                sgrambase = '%s_%s.png' % (subnet, startOfSgramTimeWindow.strftime('%Y%m%d-%H%M'))
                sgramfile = os.path.join(sgramdir, sgrambase)
                if not os.path.isdir(sgramdir):
                    os.makedirs(sgramdir)
                if not os.path.isfile(sgramfile) or overwrite:
                    f"Output file: {sgramfile}"
                    spobj = IceWeb.icewebSpectrogram(stream=tw_st)
                    fh, ah = spobj.plot(outfile=sgramfile, dbscale=dbscale, title=sgramfile, equal_scale=equal_scale, clim=clim, fmin=freqmin, fmax=freqmax)
                    try:
                        fh.close()
                    except:
                        plt.close()

                startOfSgramTimeWindow += sgrammins * 60    

        else: # No inventory, just raw RSAM
            thisSDSobj.read(startOfRsamTimeWindow, endOfRsamTimeWindow, speed=2, trace_ids=trace_ids)
            if verbose:
                f"SDS Stream: {thisSDSob.stream}"
                f"Computing raw RSAM"
            thisRSAMobj = IceWeb.RSAMobj(st=thisSDSobj.stream, sampling_interval=sampling_interval, freqmin=freqmin, freqmax=freqmax, \
                               zerophase=zerophase, corners=corners, verbose=verbose, startt=startt, endt=endOfRsamTimeWindow, units='Counts', absolute=True)
            if verbose:
                f"Saving raw RSAM to SDS"
            thisRSAMobj.write(SDS_TOP) # write RSAM to an SDS-like structure

        startOfRsamTimeWindow+=rsamStepSize # add 1 day 
        






def SDS_to_picklefile_wrapper(startt, endt, SDS_TOP, freqmin=0.5, freqmax=None, \
        zerophase=False, corners=2, sampling_interval=60.0, sourcelat=None, \
            sourcelon=None, inv=None, trace_ids=None, overwrite=True, verbose=False, timeWindowMinutes=10,  timeWindowOverlapMinutes=5, PICKLEDIR='.', subnet='unknown'):
    '''
    Load Stream from SDS archive and create pickle files each containing an instrument-corrected Stream object, including distance metrics.This pickle filesRSAM by default is the mean absolute value in each 60-s window.
    
    For each timewindow, two pickle files are saved: a Stream containing a velocity seismogram, and a Stream containing a displacement seismogram. 
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
            PICKLEDIR (str) : Directory to save pickle files too
            subnet (str) : a label to use for this particular set of N.S.L.C.'s


    '''   
    taperSecs = timeWindowOverlapMinutes * 60
    startOfTimeWindow = startt
    while startOfTimeWindow < endt:
        print(f"Processing {startOfTimeWindow}")
        endOfTimeWindow = startOfTimeWindow + timeWindowMinutes * 60
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
                picklebase = '%s_%s_%s.pickle' % (subnet, startOfTimeWindow.strftime('%Y%m%d-%H%M'), seismogramType)
                picklefile = os.path.join(PICKLEDIR, picklebase)
                cst.write(picklefile, format='PICKLE')

                del cst, picklefile, picklebase

            del st, r, pre_filt
        gc.collect()
        startOfTimeWindow = endOfTimeWindow

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))    

def picklefileGobblerToIceweb(PICKLEDIR, verbose=False, rsamSamplingIntervalSeconds=60, RSAM_SDS_TOP='.', SGRAM_TOP='.', dbscale=True, \
                              equal_scale=True, clim=[1e-8,1e-5], fmin=0.5, fmax=None, overwrite=False, subnet='unknown'):
    '''
    Gobble up any picklefiles found and process them into IceWeb products.

    The advantage of decoupling the picklefile creation from product generation is that other processes can put picklefiles in the same directory, 
    regardless of datasource (FDSN, SDS, EWS/WWS/OWD, Seedlink, Antelope archive, Seisan archive, etc.) and regardless of whether they are running
    on real-time or archived data. They will be gobbled and then deleted. The problem would arise if picklefiles are created much faster than they
    can be consumed by the gobbler. In that case, we need to extend this function to allow multiple gobblers at the same time without stepping on 
    each other (run multiple instances of this function at the same time). This would come close to mimicing the IceWeb real-time system that was
    running at UAF 2009-2013 (I only noticed it stopped running in 2023).

    '''
 
    while True:
          counter=0
          picklefilelist = sorted_ls(PICKLEDIR) # make list of picklefiles
          #print(f"{picklefilelist}")
          if len(picklefilelist)>0:
            counter=0
            picklefile = os.path.join(PICKLEDIR, picklefilelist[0])
            print(f"Processing {picklefile}")
            if '.pickle' in picklefile:
                try:
                    st = read(picklefile, format='PICKLE')
                except Exception as e:
                    print(f"{e}")
                    continue
                if isinstance(st, Stream) and len(st)>0 and st[0].stats.npts>1000:
                    pass
                else:
                    print(f"Not a valid Stream object: {st}")
                    del st
                    os.remove(picklefile) # delete file
                    continue # next while loop iteration


                ####################################
                if 'VEL' in picklefile: 
                    
                    # compute & save instrument-corrected RSAM
                    if verbose:
                        print(f"Computing corrected RSAM")
                    thisRSAMobj = IceWeb.RSAMobj(st=st, sampling_interval=rsamSamplingIntervalSeconds, verbose=verbose,  units='m/s', absolute=True)
                    if verbose:
                        print(f"Saving corrected RSAM to SDS")
                    thisRSAMobj.write(RSAM_SDS_TOP) # write RSAM to an SDS-like structure
                    del thisRSAMobj

                    # Spectrogram
                    startt = st[0].stats.starttime
                    #endt = st[0].stats.endtime
                    sgramdir = os.path.join(SGRAM_TOP, st[0].stats.network, startt.strftime('%Y'), startt.strftime('%j'))
                    sgrambase = '%s_%s.png' % (subnet, startt.strftime('%Y%m%d-%H%M'))
                    sgramfile = os.path.join(sgramdir, sgrambase)
                    if not os.path.isdir(sgramdir):
                        os.makedirs(sgramdir)
                    if not os.path.isfile(sgramfile) or overwrite:
                        print(f"Output file: {sgramfile}")
                        spobj = IceWeb.icewebSpectrogram(stream=st)
                        spobj.plot(outfile=sgramfile, dbscale=dbscale, title=sgramfile, equal_scale=equal_scale, clim=clim, fmin=fmin, fmax=fmax)
                        del spobj
                    plt.close('all')

                    del startt, sgramdir, sgrambase, sgramfile

                ###########################################
                elif 'DISP' in picklefile:
                     # compute/write reduced displacement
                    if verbose:
                        print(f"Computing DRS")
                    thisDRSobj = IceWeb.ReducedDisplacementObj(st=st, sampling_interval=rsamSamplingIntervalSeconds, verbose=verbose, units='m' )
                    if verbose:
                        print(f"Writing DRS to SDS")
                    thisDRSobj.write(RSAM_SDS_TOP) # write Drs to an SDS-like structure
                    del thisDRSobj
                del st
                
                # delete file
                os.remove(picklefile)

                gc.collect()

          else:
              if counter==0:
              	f"Waiting for new pickle file"  
              else:
                print('.', end='')
                
              counter += 1    


import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
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


def create_iceweb_index_db(dbpath):

    sql_create_index_table = """ CREATE TABLE IF NOT EXISTS icewebindex (
                                        subnet text NOT NULL,
                                        startTime integer NOT NULL,
                                        endTime integer,
                                        rsamDone integer,
                                        drsDone integer,
                                        sgramDone integer,
                                        PRIMARY KEY (subnet, startTime, endTime)
                                    ); """


    # create a database connection
    conn = create_connection(dbpath)
    print(conn)

    # create tables
    if conn is not None:
        # create index table
        create_table(conn, sql_create_index_table)
    else:
        print("Error! cannot create the database connection.")
        create_table(conn, sql_create_index_table)
    return conn

def insert_index_row(conn, indexrow):
    """
    Create a new index row into the index table
    :param conn:
    :param indexrow
    :return: did it work (True, False)
    """
    sql = ''' INSERT INTO icewebindex(subnet, startTime, endTime, rsamDone, drsDone, sgramDone)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, indexrow)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False

def select_indexrow_by_primary_key(conn, subnet, startTime):
    """
    Query tasks by subnet, startTime
    :param conn: the Connection object
    :param subnet:
    :param startTime:
    :return:

    Can use this to check if rsamDone, drsDone, sgramDone, etc.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM icewebindex WHERE subnet=? AND startTime=?", (subnet,startTime))

    rows = cur.fetchall()
    if len(rows)==1:
        print(rows[0])
        return rows[0] # a tuple


def update_fieldDone(conn, subnet, startTime, field='rsamDone', value=True):
    """
    Query tasks by subnet, startTime
    :param conn: the Connection object
    :param subnet:
    :param startTime:
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"UPDATE icewebindex set {field}=? WHERE subnet=? AND startTime=?", (value, subnet, startTime))
    conn.commit()




if __name__ == '__main__':
    dbpath = '/RAIDZ/IceWeb/iceweb_sqllite3.db'
    conn = create_iceweb_index_db(dbpath)
    subnet = 'Shishaldin'
    stime = 1696454518
    etime = stime + 600
    if conn is not None:
        indexrow = ('Shishaldin', stime, etime, False, False, False)
        diditwork = insert_index_row(conn, indexrow) # diditwork False if unique row already exists
        matchingrow = select_indexrow_by_primary_key(conn, subnet, stime)
        update_fieldDone(conn, subnet, stime, field='rsamDone')
        matchingrow = select_indexrow_by_primary_key(conn, subnet, stime)
        update_fieldDone(conn, subnet, stime, field='sgramDone')
        matchingrow = select_indexrow_by_primary_key(conn, subnet, stime)
        conn.close()

