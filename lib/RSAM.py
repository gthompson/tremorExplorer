import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from obspy.core import read, Stream, UTCDateTime


class RSAMmetrics:
    def __init__(self, st=None, sampling_interval=60.0, absolute=True, filter=True):
        ''' Compute RSAM metrics. You must pass a Stream object that has already been detrended, high pass filtered, instrument corrected '''
        self.dataframes = {} 
        self.trace_ids = []
        
        if isinstance(st, Stream):
            bands = {'VLP': [0.02, 0.2], 'LP':[0.5, 4.0], 'VT':[4.0, 18.0]}
            for tr in st:
                print(tr.id, 'absolute=',absolute)
                df = pd.DataFrame()
                
                t = tr.times('timestamp') # Unix epoch time
                sampling_rate = tr.stats.sampling_rate
                t = reshape_trace_data(t, sampling_rate, sampling_interval, absolute=False)
                df['time'] = pd.Series(np.nanmin(t,axis=1))

                if filter:
                    tr_normal = tr.copy().filter('highpass', freq=0.5)
                    y = reshape_trace_data(tr_normal.data, sampling_rate, sampling_interval, absolute=absolute)
                else:
                    y = reshape_trace_data(tr.data, sampling_rate, sampling_interval, absolute=absolute)
                #if absolute:
                #    y = abs(y)
                df['min'] = pd.Series(np.nanmin(y,axis=1))    
                df['mean'] = pd.Series(np.nanmean(y,axis=1)) 
                df['max'] = pd.Series(np.nanmax(y,axis=1))
                df['median'] = pd.Series(np.nanmedian(y,axis=1))
                if filter and absolute:
                    for key in bands:
                        tr2 = tr.copy()
                        [flow, fhigh] = bands[key]
                        tr2.filter('bandpass', freqmin=flow, freqmax=fhigh, corners=2)
                        y = reshape_trace_data(tr2.data, sampling_rate, sampling_interval, absolute=absolute)
                        df[key] = pd.Series(np.nanmean(y,axis=1))
                self.dataframes[tr.id] = df
                self.trace_ids.append(tr.id)

    def write(self, RSAM_TOP='.'):
        for key in self.dataframes:
            df = self.dataframes[key]
            if df.empty:
                continue
            starttime = df.iloc[0]['time']
            yyyy = UTCDateTime(starttime).year
            rsam_csv = os.path.join(RSAM_TOP,'RSAM_metrics_%s_%4d.csv' % (key, yyyy))
            if not os.path.isdir(RSAM_TOP):
                os.makedirs(RSAM_TOP)
            print(f"Saving to {rsam_csv}")
            if os.path.isfile(rsam_csv):
                original_df = pd.read_csv(rsam_csv)
                combined_df = pd.concat([original_df, df], ignore_index=True)
                combined_df = combined_df.drop_duplicates(subset=['time'], keep='last')
                combined_df.to_csv(rsam_csv, index=False)
            else:
                df.to_csv(rsam_csv, index=False)

    def plot(self, metrics=None, log=False, kind='line'):
        i = 0
        for key in self.dataframes:
            df = self.dataframes[key]
            this_df = df.copy()
            if metrics:
                this_df = this_df[metrics]
            this_df['time'] = pd.to_datetime(df['time'], unit='s')
            if kind == 'line':
                ph = this_df.plot(x='time', y=['mean', 'median'], kind='line', title=self.trace_ids[i], logy=log, rot=45)
            elif kind  == 'scatter':
                fh, ax = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=False)
                this_df.plot(x='time', y='mean', kind=kind, ax=ax[0], title=self.trace_ids[i], logy=log, rot=45)
                this_df.plot(x='time', y='median', kind=kind, ax=ax[1], title=self.trace_ids[i], logy=log, rot=45)
            plt.show()
            if 'VLP' in this_df.columns:
                if kind=='line':
                    ph2 = this_df.plot(x='time', y=['VLP', 'LP', 'VT'], kind='line', title=f"{self.trace_ids[i]}, f-bands", logy=log, rot=45)
                elif kind=='scatter':
                    fh2, ax2 = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=False)
                    this_df.plot(x='time', y='VLP', kind='scatter', ax=ax2[0], title=f"{self.trace_ids[i]}, f-bands", logy=log, rot=45)
                    this_df.plot(x='time', y='LP', kind='scatter', ax=ax2[1], title=f"{self.trace_ids[i]}, f-bands", logy=log, rot=45)
                    this_df.plot(x='time', y='VT', kind='scatter', ax=ax2[2], title=f"{self.trace_ids[i]}, f-bands", logy=log, rot=45)
                plt.show()
            plt.close('all')
                
            i += 1
        

def read_RSAMmetrics(startt, endt, trace_ids=None, RSAM_TOP='.'):
    self = RSAMmetrics()
    if not endt.year == startt.year:
        print('Cannot read across year boundaries. Adjusting to end of start year')
        endt = obspy.UTCDateTime(startt.year, 12, 31, 23, 59, 59)
    yyyy = startt.year
    if not trace_ids:
        # find all matching files
        import glob
        rsamfiles = glob.glob(os.path.join(RSAM_TOP,'RSAM_metrics_*_[0-9][0-9][0-9][0-9].csv'))
        trace_ids = []
        for rsam_csv in rsamfiles:
            parts = rsam_csv.split('_')
            trace_ids.append(parts[-2])
    else:
        rsamfiles = []
        for id in trace_ids:
            rsamfiles.append(os.path.join(RSAM_TOP,'RSAM_metrics_%s_%4d.csv' % (id, yyyy)))
    for i, rsam_csv in enumerate(rsamfiles):
        id = trace_ids[i]
        try:
            print(rsam_csv)
            df = pd.read_csv(rsam_csv, index_col=False)
        except:
            if df.empty:
                continue
        df['pddatetime'] = pd.to_datetime(df['time'], unit='s')
        # construct Boolean mask
        mask = df['pddatetime'].between(startt.isoformat(), endt.isoformat())
        # apply Boolean mask
        subset_df = df[mask]
        self.dataframes[id] = subset_df.drop(columns=['pddatetime'])
        self.trace_ids.append(id)
    return self

def reshape_trace_data(x, sampling_rate, sampling_interval, absolute=True):
    # reshape the data vector into an array, so we can take advantage of np.mean()
    if absolute:
        x = np.absolute(x)
        #x = abs(x)
    s = np.size(x) # find the size of the data vector
    nc = int(sampling_rate * sampling_interval) # number of columns
    nr = int(s / nc) # number of rows
    x = x[0:nr*nc] # cut off any trailing samples
    y = x.reshape((nr, nc))
    if absolute:
        y = np.absolute(y) # this should be obsolete
    return y
    

class ReducedDisplacementObj(): # SCAFFOLD: Modify this from old RSAMob model to new RSAMmetrics model
    # Difference from RSAM is 
    # (1) Correct to displacement first 
    # (2) Filter, 
    # (3) Apply geometric spreading 
    # (4) Correct for Q
    def __init__(self, st=None, inv=None, sampling_interval=60.0, verbose=False, metric='median', \
            freqmin=0.5, freqmax=15.0, zerophase=False, corners=2, peakf=2.0, wavespeed=2000, sourcelat=None, sourcelon=None, \
                 startt=None, endt=None, units=None ):
        self.stream = Stream()
        self.metric = metric

        try:
            r = [tr.stats.distance for tr in st]
            if not r:
                InventoryTools.attach_station_coordinates_from_inventory(inv, st)
                InventoryTools.attach_distance_to_stream(st, sourcelat, sourcelon) 
            if not r:
                f"Cannot determine distances from source to stations"
                return
        except:
            f"Cannot determine distances from source to stations"
            return           

        if units=='Counts' and inv: # try to correct          
            for tr in st:
                if tr.stats.channel[2] in 'ENZ' : # filter seismic channels only
                    print('Processing %s' % tr.id)
                    if inv:
                        pre_filt = [freqmin/1,2, freqmin, freqmax, freqmax*1.2]
                        tr.remove_response(output='DISP', inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)    
                        self.corrected = True
                        if startt:
                            tr.trim(starttime=startt, endtime=endt)
        elif units=='m':
                print('Units suggest this is already a displacement seismogram. No filtering or instrument correction performed.')
                
        else:
                print('Cannot compute Drs. Need to know units.')
                return

        # We now have Displacement seismogram
        for tr in st:
            this_tr = tr.copy()
            x = (tr.data*100) * np.sqrt(tr.stats.distance*100 * peakf * wavespeed * 100) # everything in cm
            # now we want to reshape the data vector into an array, so we can take advantage of np.mean()
            s = np.size(x) # find the size of the data vector
            nc = int(tr.stats.sampling_rate * sampling_interval) # number of columns
            nr = int(s / nc) # number of rows
            x = x[0:nr*nc] # cut off any trailing samples
            y = x.reshape((nr, nc))
            if verbose:
                print('%s: size %d' % (tr.id, s))
                print('%s: reshaped to %d x %d array (%d samples)' % (tr.id, nr, nc, nr * nc))
            if metric=='mean':
                this_tr.data = np.nanmean(abs(y),axis=1) # compute mean for each row (this is vectorised; faster than a for loop)
            if metric=='median':
                this_tr.data = np.nanmedian(abs(y),axis=1) # compute mean for each row (this is vectorised; faster than a for loop)
            if metric=='max':
                this_tr.data = np.nanmax(abs(y),axis=1) # compute mean for each row (this is vectorised; faster than a for loop)
            if metric=='rms':
                this_tr.data = np.rms(abs(y),axis=1) # compute mean for each row (this is vectorised; faster than a for loop)     
            this_tr.stats.sampling_rate = 1.0 / sampling_interval # update the sampling rate
            self.stream.append(this_tr)
        self.sampling_interval = sampling_interval



    def plot(self, equal_scale=False, type='linear', percentile=None, linestyle='-'):
        st = self.stream.copy()
        for tr in st:
            tr.data = np.where(tr.data==0, np.nan, tr.data)
        if type=='linear':
            linearplot(st, equal_scale=equal_scale, percentile=percentile, linestyle=linestyle)
        elif type=='log':
            import matplotlib.pyplot as plt
            import matplotlib.dates as mdates
            from math import log2
            plt.rcParams["figure.figsize"] = (10,6)
            fig, ax = plt.subplots()
            for tr in st:
                x = tr.data
                 # now we want to reshape the data vector into an array, so we can take advantage of np.mean()
                s = np.size(x) # find the size of the data vector
                nc = np.max((1, int(log2(s/260))))  # number of columns
                #nc = nc * 4
                nr = int(s / nc) # number of rows
                x = x[0:nr*nc] # cut off any trailing samples
                y = x.reshape((nr, nc))
                y2 = np.nanmax(y,axis=1)    
                t = tr.times("utcdatetime")[::nc]   
                t = [this_t.datetime for this_t in t] 
                #print(t) 
                t = t[:len(y2)]      
                ax.semilogy(t, y2,linestyle, label='%s' % tr.id) #, alpha=0.03)
            ax.format_xdata = mdates.DateFormatter('%H')
            ax.legend()
            plt.xticks(rotation=45)
            plt.ylim((0.2, 100)) # IceWeb plots went from 0.05-30
            plt.yticks([0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0], \
                ['0.2', '0.5', '1', '2', '5', '10', '20', '50', '100'])
            plt.ylabel(r'$D_{RS}$ ($cm^{2}$)')
            plt.xlabel(r'UTC / each point is max $D_{RS}$ in %d minute window' % (tr.stats.delta * nc /60))
            plt.title('Reduced Displacement (%s)\n%s to %s' % (r'$D_{RS}$', t[0].strftime('%d-%b-%Y %H:%M:%S UTC'), t[-1].strftime('%d-%b-%Y %H:%M:%S UTC')))
        return 0   


    def write(self, SDS_TOP):
        DrsSDS_TOP = os.path.join(SDS_TOP,'DRS',self.metric)
        DrsSDSobj = SDS.SDSobj(DrsSDS_TOP, streamobj=self.stream)
        DrsSDSobj.write(overwrite=True)                
    
    def read(self, startt, endt, SDS_TOP, metric='mean', speed=2):
        DrsSDS_TOP = os.path.join(SDS_TOP,'DRS',self.metric)
        thisSDSobj = SDS.SDSobj(DrsSDS_TOP)
        thisSDSobj.read(startt, endt, speed=speed)
        print(thisSDSobj.stream)
        self.stream = thisSDSobj.stream
        self.metric=metric
        self.sampling_interval=self.stream[0].stats.delta  




def linearplot(st, equal_scale=False, percentile=None, linestyle='-'):
    hf = st.plot(handle=True, equal_scale=equal_scale, linestyle=linestyle) #, method='full'); # standard ObsPy plot
    # change the y-axis so it starts at 0
    allAxes = hf.get_axes()
    ylimupper = [ax.get_ylim()[1] for ax in allAxes]
    print(ylimupper)
    if percentile:
        ylimupper = np.array([np.percentile(tr.data, percentile) for tr in st])*1.1
    # if equal_scale True, we set to maximum scale
    print(ylimupper)
    ymax=max(ylimupper)
    for i, ax in enumerate(allAxes):
        if equal_scale==True:
            ax.set_ylim([0, ymax])
        else:
            ax.set_ylim([0, ylimupper[i]])  

if __name__ == "__main__":
    print("This is the RSAM module. It also handles Reduced Displacement")
    print('Example: RSAM_wrapper_Shishaldin.ipynb on 2023/08/31')




