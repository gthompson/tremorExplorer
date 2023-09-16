import os
import numpy as np
from obspy import Stream
import obspyGT.SDS
from obspyGT.InventoryTools import attach_station_coordinates_from_inventory, attach_distance_to_stream


class RSAMobj:
    
    def __init__(self, st=None, inv=None, sampling_interval=60.0, verbose=False, metric='mean', freqmin=0.5, freqmax=15.0, zerophase=False, corners=2, startt=None, endt=None, abs=True, last_ylist=None, units=Counts ):
        self.stream = Stream()
        self.metric = metric
        self.corrected = False
        y_list = []
        if isinstance(st, Stream):
            for index,tr in enumerate(st):
                if last_ylist:
                    y = last_ylist[index]
                else:
                    if tr.stats.channel[2] in 'ENZ' or tr.stats.channel[1:]=='DF': # filter seismic and infrasound channels only
                        print('Processing %s' % tr.id)
                        if inv and units=='Counts':
                            pre_filt = [freqmin/1.2, freqmin, freqmax, freqmax*1.2]
                            tr.remove_response(output='VEL', inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)    
                            self.corrected = True
                        elif units=='m/s':
                            pass
                        elif units=='Counts':
                            tr.detrend(type='linear')
                            tr.filter('bandpass', freqmin=freqmin, freqmax=freqmax, zerophase=False, corners=corners)                            
                            print('No inventory for RSAM calculation. Only detrended & bandpassed.')  
                    if startt:                               
                        tr.trim(starttime=startt, endtime=endt) # in case extra padding applied for instrument response removal. sometimes we send 26 hours of data 1-24-1 so no taper at start and end of day
                    this_tr = tr.copy()
                    x = tr.data # get the data
                    # now we want to reshape the data vector into an array, so we can take advantage of np.mean()
                    s = np.size(x) # find the size of the data vector
                    nc = int(tr.stats.sampling_rate * sampling_interval) # number of columns
                    nr = int(s / nc) # number of rows
                    x = x[0:nr*nc] # cut off any trailing samples
                    y = x.reshape((nr, nc))
                    if abs:
                        y = abs(y)
                y_list(append(y))


                if verbose:
                    print('%s: size %d' % (tr.id, s))
                    print('%s: reshaped to %d x %d array (%d samples)' % (tr.id, nr, nc, nr * nc))
                    print(tr.stats)     
           
                if metric=='mean':
                    this_tr.data = np.nanmean(y,axis=1) # compute mean for each row (this is vectorised; faster than a for loop)
                if metric=='median':
                    this_tr.data = np.nanmedian(y,axis=1) # compute median for each row (this is vectorised; faster than a for loop)
                if metric=='max':
                    this_tr.data = np.nanmax(y,axis=1) # compute max for each row (this is vectorised; faster than a for loop)
                if metric=='rms':
                    this_tr.data = np.rms(y,axis=1) # compute min for each row (this is vectorised; faster than a for loop)     
                this_tr.stats.sampling_rate = 1.0 / sampling_interval # update the sampling rate
                self.stream.append(this_tr)
        self.sampling_interval = sampling_interval
        return y_list

    def plot(self, equal_scale=False, type='linear', percentile=None, linestyle='-'):
        st = self.stream.copy()
        for tr in st:
            tr.data = np.where(tr.data==0, np.nan, tr.data)
        if type=='linear':
            linearplot(st, equal_scale=equal_scale, percentile=percentile, linestyle=linestyle)


    def _fix_traceid(self):
        # See: https://ds.iris.edu/ds/nodes/dmc/data/formats/seed-channel-naming/
        for tr in self.stream:
            if tr.stats.delta == 1:
                tr.stats.channel = 'L' + tr.stats.channel[1:]
            if tr.stats.delta == 60:
                tr.stats.channel = 'V' + tr.stats.channel[1:]
            if tr.stats.delta == 600:
                tr.stats.channel = 'U' + tr.stats.channel[1:]          


    def write(self, SDS_TOP):
        if self.corrected:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'CSAM',self.metric)
        else:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'RSAM',self.metric)            
        #self._fix_traceid()
        RSAMSDSobj = obspyGT.SDS.SDSobj(RSAMSDS_TOP, streamobj=self.stream)
        RSAMSDSobj.write(overwrite=True)           
        
    
    def read(self, startt, endt, SDS_TOP, metric='mean', speed=2, corrected=False):
        if corrected:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'CSAM',self.metric)
        else:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'RSAM',self.metric)           
        thisSDSobj = obspyGT.SDS.SDSobj(RSAMSDS_TOP)
        thisSDSobj.read(startt, endt, speed=speed)
        print(thisSDSobj.stream)
        self.stream = thisSDSobj.stream
        self.metric=metric
        if len(self.stream)>0:
            self.sampling_interval=self.stream[0].stats.delta



class ReducedDisplacementObj():
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



        if units=='Counts' and inv:
            if not sourcelat or not sourcelon:
                print('Need a seismic source location to compute distances.')
            pre_filt = [freqmin*2/3, freqmin, freqmax, freqmax*1.5]
            attach_station_coordinates_from_inventory(inv, st)
            attach_distance_to_stream(st, sourcelat, sourcelon)            
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


    def _fix_traceid(self):
        # See: https://ds.iris.edu/ds/nodes/dmc/data/formats/seed-channel-naming/
        for tr in self.stream:
            if tr.stats.delta == 1:
                tr.stats.channel = 'L' + tr.stats.channel[1:]
            if tr.stats.delta == 60:
                tr.stats.channel = 'V' + tr.stats.channel[1:]
            if tr.stats.delta == 600:
                tr.stats.channel = 'U' + tr.stats.channel[1:]          


    def write(self, SDS_TOP):
        DrsSDS_TOP = os.path.join(SDS_TOP,'DRS',self.metric)
        #self._fix_traceid()
        DrsSDSobj = obspyGT.SDS.SDSobj(DrsSDS_TOP, streamobj=self.stream)
        DrsSDSobj.write(overwrite=True)                
    
    def read(self, startt, endt, SDS_TOP, metric='mean', speed=2):
        DrsSDS_TOP = os.path.join(SDS_TOP,'DRS',self.metric)
        thisSDSobj = obspyGT.SDS.SDSobj(DrsSDS_TOP)
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