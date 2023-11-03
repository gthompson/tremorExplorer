from obspy.core import read, Stream, UTCDateTime
import numpy as np
import pandas as pd

## imports for mimicing obspy spectrograms
from obspy.imaging.spectrogram import _nearest_pow_2
from matplotlib import mlab
import matplotlib as mpl
import matplotlib.pyplot as plt

# colormaps. See https://docs.obspy.org/packages/autogen/obspy.imaging.cm.html
from obspy.imaging.cm import pqlx

# adding colorbar
from mpl_toolkits.axes_grid1 import make_axes_locatable

# for spectrum
from scipy import interpolate

# for wrappers - might split off into their own module
import SDS
import InventoryTools
import os

class icewebSpectrogram:
    
    def __init__(self, stream=None, secsPerFFT=-1):
        """
        :type st: Stream
        :param st: an ObsPy Stream object. No detrending or filtering is done, so do that before calling this function.
        """
        self.stream = Stream()
        self.precomputed = False
        if isinstance(stream, Stream):
            self.stream = stream
            count = 0
            for tr in self.stream:
                if 'spectrogramdata' in tr.stats:
                    count += 1
    
            if len(self.stream)==count:
                self.precomputed = True
       
    def __str__(self):
        str = '\n\nicewebSpectrogram:\n'
        str += self.stream.__str__()
        #str += '\nF: %d 1-D numpy arrays' % len(self.F)
        #str += '\nT: %d 1-D numpy arrays' % len(self.T)
        #str += '\nS: %d 2-D numpy arrays\n\n' % len(self.S)
        return str
    
    def precompute(self, secsPerFFT=None):
        """
    
        For each Trace in self.stream, call compute_spectrogram. T,F and S arrays will be saved in tr.stats.spectrogramdata
    
        :type secsPerFFT: int or float
        :param secsPerFFT: Window length for fft in seconds. If this parameter is too
            small, the calculation will take forever. If None, it defaults to
            ceil(sampling_rate/100.0).
        """

        # seconds to use for each FFT. 1 second if the event duration is <= 100 seconds, 6 seconds if it is 10-minutes
        if secsPerFFT is None:
            secsPerFFT = np.ceil((self.stream[0].stats.delta * self.stream[0].stats.npts)/100) 
        
        for tr in self.stream:
            [T, F, S] = compute_spectrogram(tr, wlen=secsPerFFT)
            tr.stats['spectrogramdata'] = {'T':T, 'F':F, 'S':S}
        self.precomputed = True
    
        return self    

    
    def plot(self, outfile=None, secsPerFFT=None, fmin=0.5, fmax=20.0, log=False, cmap=pqlx, clim=None, \
                      equal_scale=False, title=None, add_colorbar=True, precompute=False, dbscale=False, trace_indexes=[] ):   
        """
        For each Trace in a Stream, plot the seismogram and spectrogram. This results in 2*N subplots 
        on the figure, where N is the number of Trace objects.
        This is modelled after IceWeb spectrograms, which have been part of the real-time monitoring 
        system at the Alaska Volcano Observatory since March 1998
        MATLAB code for this exists in the GISMO toolbox at 
        https://github.com/geoscience-community-codes/GISMO/blob/master/applications/+iceweb/spectrogram_iceweb.m
    
        :type outfile: str
        :param outfile: String for the filename of output file     
        :type fmin: float
        :param fmin: frequency minimum to plot on spectrograms
        :type fmax: float
        :param fmax: frequency maximum to plot on spectrograms    
        :type log: bool
        :param log: Logarithmic frequency axis if True, linear frequency axis
            otherwise.
        :type cmap: :class:`matplotlib.colors.Colormap`
        :param cmap: Specify a custom colormap instance. If not specified, then the
            pqlx colormap is used. viridis_white_r might be worth trying too.
        :type clim: [float, float]
        :param clim: colormap limits. adjust colormap to clip at lower and/or upper end.
            This overrides equal_scale parameter.
        :type equal_scale: bool
        :param equal_scale: Apply the same colormap limits to each spectrogram if True. 
            This requires more memory since all spectrograms have to be pre-computed 
            to determine overall min and max spectral amplitude within [fmin, fmax]. 
            If False (default), each spectrogram is individually scaled, which is best 
            for seeing details. equal_scale is overridden by clim if given.
        :type add_colorbar: bool
        :param add_colorbar: Add colorbars for each spectrogram (5% space will be created on RHS)        
        :type title: str
        :param title: String for figure super title
        :type dbscale: bool
        :param dbscale: If True 20 * log10 of color values is taken. 
        :type trace_indexes: list of int (or None:default)
        :param trace_indexes: Only plot spectrograms for these trace indexes, if set.
        """
        
        if not self.precomputed and precompute:
            self = self.precompute(secsPerFFT=secsPerFFT)
        
        st = self.stream
        if len(trace_indexes)>0: # same logic as metrics.select_by_index_list(st, chosen)
            st = Stream()
            for i, tr in enumerate(self.stream):
                if i in trace_indexes:
                    st.append(tr)

        N = len(st) # number of channels we are plotting        
        if N==0:
            print('Stream object is empty. Nothing to do')
            return
         
        fig, ax = plt.subplots(N*2, 1); # create fig and ax handles with approx positions for now
        fig.set_size_inches(5.76, 7.56); 

        if clim:
            if clim[0]<=clim[1]/100000:
                print('Warning: Lower clim should be at least 1/10000 of Upper clim. This translates to a 100 dB range in amplitude')
                clim[0]=clim[1]/100000
 
        if equal_scale and not clim: # calculate range of spectral amplitudes
            if self.precomputed:
                Smin, Smax = icewebSpectrogram.get_S_range(self, fmin=fmin, fmax=fmax)
            else:
                index_min = np.argmin(st.max()) # find the index of largest Trace object
                [T, F, S] = compute_spectrogram(st[index_min], wlen=secsPerFFT)
                f_indexes = np.intersect1d(np.where(F>=fmin), np.where(F<fmax))
                S_filtered = S[f_indexes, :]
                Smax = np.nanmax(S_filtered)
                S_filtered[S_filtered == 0] = Smax
                Smin = np.nanmin(S_filtered)
                
            if Smin<Smax*1e-6: # impose a dynamic range limit of 1,000,000
                Smin=Smax*1e-6
                
            clim = (Smin, Smax)
        
        for c, tr in enumerate(st):
            if self.precomputed: 
                T = tr.stats.spectrogramdata.T
                F = tr.stats.spectrogramdata.F
                S = tr.stats.spectrogramdata.S          
            else:                
                [T, F, S] = compute_spectrogram(tr, wlen=secsPerFFT)
        
            # fix the axes positions for this trace and spectrogram, making space for a colorbar at bottom if using a fixed scale
            if add_colorbar and clim:
                spectrogramPosition, tracePosition = icewebSpectrogram.calculateSubplotPositions(N, c, 
                                                                       frameBottom = 0.17, totalHeight = 0.80)
                #cax = fig.add_axes([spectrogramPosition[0], 0.08, spectrogramPosition[2], 0.02])
                #cax.set_xticks([])
                #cax.set_yticks([])


            else:
                spectrogramPosition, tracePosition = icewebSpectrogram.calculateSubplotPositions(N, c)
            ax[c*2].set_position(tracePosition)
            ax[c*2+1].set_position(spectrogramPosition)
        
            # plot the trace
            t = tr.times()
            ax[c*2].plot(t, tr.data, linewidth=0.5);
            ax[c*2].set_yticks(ticks=[]) # turn off yticks
        
            if log:
                # Log scaling for frequency values (y-axis)
                ax[c*2+1].set_yscale('log')
           
            # Plot spectrogram
            vmin = None
            vmax = None
            if clim:
                if dbscale:
                    vmin, vmax = amp2dB(clim)
                else:
                    vmin, vmax = clim
            if dbscale:
                S = amp2dB(S)
            
            #print(vmin, vmax)
            sgram_handle = ax[c*2+1].pcolormesh(T, F, S, vmin=vmin, vmax=vmax, cmap=cmap );
            ax[c*2+1].set_ylim(fmin, fmax)

            # turn off xticklabels, except for bottom panel
            ax[c*2].set_xticklabels([])
            if c<N-1:
                ax[c*2+1].set_xticklabels([])

            # add a ylabel
            ax[c*2+1].set_ylabel('     ' + tr.stats.station + '.' + tr.stats.channel, rotation=80)
        
            # Plot colorbar
            if add_colorbar:
                if clim: # Scaled. Add a colorbar at the bottom of the figure. Just do it once.
                    if c==0:
                        #fig.colorbar(sgram_handle, cax=cax, orientation='horizontal'); 
                        norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
                        #cax = fig.add_axes([0.2, 0.1, 0.6, 0.05])
                        cax = fig.add_axes([spectrogramPosition[0], 0.08, spectrogramPosition[2], 0.02])
                        cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation='horizontal', label='Counts/Hz')
                        if dbscale:
                            cax.set_xlabel('dB relative to 1 m/s/Hz')
                            ''' 
                            # Failed attempt to add a second set of labels to top of colorbar
                            # It just wipes out the original xtick labels
                            cax2 = cax.twinx()
                            cax2.xaxis.set_ticks_position("top")
                            xticks = cax.get_xticks()
                            xticks = np.power(xticks/20, 10)
                            cax2.set_xticks(xticks)
                            cax2.set_xlabel('m/s/Hz')
                            '''
                        else:
                            cax.set_xlabel('m/s/Hz')
                else: # Unscaled, so each spectrogram has max resolution. Add a colorbar to the right of each spectrogram.
                    divider = make_axes_locatable(ax[c*2+1])
                    cax = divider.append_axes("right", size="5%", pad=0.05)
                    fig.colorbar(sgram_handle, cax=cax);
                    # also add space next to Trace
                    divider2 = make_axes_locatable(ax[c*2])
                    hide_ax = divider2.append_axes("right", size="5%", pad=0.05, visible=False)
                      

            

            
            # increment c and go to next trace (if any left)
            c += 1   
     
        ax[N*2-1].set_xlabel('Time [s]')
    
        if title:
            ax[0].set_title(title)
        
        # set the xlimits for each panel from the min and max time values we kept updating
        min_t = min([tr.stats.starttime for tr in st]) 
        max_t = max([tr.stats.endtime for tr in st]) - min_t        
        for c in range(N): 
            ax[c*2].set_xlim(0, max_t)
            ax[c*2].grid(axis='x', linestyle = ':', linewidth=0.5)
            ax[c*2+1].set_xlim(0, max_t)
            ax[c*2+1].grid(True, linestyle = ':', linewidth=0.5)    

        # change all font sizes
        plt.rcParams.update({'font.size': 8});    
                
        # write plot to file
        if outfile:
            fig.savefig(outfile, dpi=100)

        return fig, ax 
    
    def get_time_range(self):
        min_t = min([tr.stats.starttime for tr in self.stream]) 
        max_t = max([tr.stats.endtime for tr in self.stream]) 
        return min_t, max_t      

    def get_S_range(self, fmin=0.5, fmax=20.0):
        Smin = 999999.9
        Smax = -999999.9
        for tr in self.stream:
            F = tr.stats.spectrogramdata['F']
            S = tr.stats.spectrogramdata['S']
                            
            # filter S between fmin and fmax and then update Smin and Smax
            f_indexes = np.intersect1d(np.where(F>=fmin), np.where(F<fmax))
            try:
                S_filtered = S[f_indexes, :]
            except:
                print('S_range failed. F is ',F.shape, ' S is ',S.shape)
            else:
                Smin = np.nanmin([np.nanmin(S_filtered), Smin])
                Smax = np.nanmax([np.nanmax(S_filtered), Smax])
        #print('S ranges from %e to %e' % (Smin, Smax))
        return Smin, Smax    
        
    def calculateSubplotPositions(numchannels, channelNum, frameLeft=0.12, frameBottom=0.08, \
                              totalWidth = 0.8, totalHeight = 0.88, fractionalSpectrogramHeight = 0.8):
        """ Copied from the MATLAB/GISMO function """
    
        channelHeight = totalHeight/numchannels;
        spectrogramHeight = fractionalSpectrogramHeight * channelHeight;
        traceHeight = channelHeight - spectrogramHeight; 
        spectrogramBottom = frameBottom + (numchannels - channelNum - 1) * channelHeight; 
        traceBottom = spectrogramBottom + spectrogramHeight;
        spectrogramPosition = [frameLeft, spectrogramBottom, totalWidth, spectrogramHeight];
        tracePosition = [frameLeft, traceBottom, totalWidth, traceHeight];
    
        return spectrogramPosition, tracePosition  

    def compute_amplitude_spectrum(self, compute_bandwidth=False):
        for c, tr in enumerate(self.stream):
            tr.stats['spectrum'] = dict()
            A = np.nanmean(tr.stats.spectrogramdata.S, axis=1)
            F = tr.stats.spectrogramdata.F
            max_i = np.argmax(A)
            tr.stats.spectrum['A'] = A
            tr.stats.spectrum['F'] = F
            tr.stats.spectrum['peakF'] = F[max_i]
            tr.stats.spectrum['peakA'] = max(A)
            tr.stats.spectrum['medianF'] = np.sum(np.dot(A, F))/np.sum(A)
            if compute_bandwidth:
                try:
                    Athresh = max(A)*0.707          
                    fn = interpolate.interp1d(F,  A)
                    xnew = np.arange(0, max(F), 0.1)
                    ynew = fn(xnew)
                    ind = np.argwhere(ynew>Athresh)
                    tr.stats.spectrum['bw_min'] = xnew[ind[0]]
                    tr.stats.spectrum['bw_max'] = xnew[ind[-1]]
                except:
                    print('Could not compute bandwidth')
            for key in tr.stats.spectrum:
                v = tr.stats.spectrum[key]
                if np.ndim(v)==1:
                    if np.size(v)==1:
                        tr.stats.spectrum[key] = v[0]

                       
    
    def plot_amplitude_spectrum(self):
        fig, ax = plt.subplots(len(self.stream), 1);
        for c, tr in enumerate(self.stream):
            if not 'spectrum' in tr.stats:
                continue
            A = tr.stats.spectrum.A   
            F = tr.stats.spectrum.F
            ax[c].semilogy(F,  A);
            ax[c].set_ylabel('Spectral Amplitude:\n%s/Hz' % tr.stats.units)
            ax[c].set_xlabel('SSAM bin (Hz?)')
            ax[c].set_title(tr.id)       
    
def compute_spectrogram(tr, per_lap=0.9, wlen=None, mult=8.0):
    """
        Computes spectrogram of the input data.
        Modified from obspy.imaging.spectrogram because we want the plotting part
        of that method in a different function to this.

        :type tr: Trace
        :param tr: Trace object to compute spectrogram for
        :type per_lap: float
        :param per_lap: Percentage of overlap of sliding window, ranging from 0
        to 1. High overlaps take a long time to compute.
        :type wlen: int or float
        :param wlen: Window length for fft in seconds. If this parameter is too
            small, the calculation will take forever. If None, it defaults to
            (samp_rate/100.0).
        :type mult: float
        :param mult: Pad zeros to length mult * wlen. This will make the
            spectrogram smoother.

    """

    Fs = float(tr.stats.sampling_rate)
    y = tr.data
    npts = tr.stats.npts
        
    # set wlen from samp_rate if not specified otherwise
    if not wlen:
        wlen = Fs / 100.0
 
    # nfft needs to be an integer, otherwise a deprecation will be raised
    nfft = int(_nearest_pow_2(wlen * Fs))
    if nfft > npts:
        nfft = int(_nearest_pow_2(npts / 8.0))

    if mult is not None:
        mult = int(_nearest_pow_2(mult))
        mult = mult * nfft
    nlap = int(nfft * float(per_lap))

    y = y - y.mean()

    # Here we do not call plt.specgram as that always produces a plot.
    # matplotlib.mlab.specgram should be faster as it computes only the arrays
    S, F, T = mlab.specgram(y, Fs=Fs, NFFT=nfft, pad_to=mult, noverlap=nlap, mode='magnitude')
        
    return T, F, S

def amp2dB(X):
    return 20 * np.log10(X)

def dB2amp(X):
    return np.power(10.0, float(X)/20.0)

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

    def plot(self, metrics=None, log=False):
        i = 0
        for key in self.dataframes:
            df = self.dataframes[key]
            this_df = df.copy()
            if metrics:
                this_df = this_df[metrics]
            this_df['time'] = pd.to_datetime(df['time'], unit='s')
            #this_df.set_index('time')
            #print(this_df.index)
            ph = this_df.plot(x='time', y=['mean', 'median'], title=self.trace_ids[i], logy=log) #, x_compat=True)
            if 'VLP' in this_df.columns:
                ph2 = this_df.plot(x='time', y=['VLP', 'LP', 'VT'], title=f"{self.trace_ids[i]}, f-bands", logy=log) #, x_compat=True)
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
    
class RSAMobj:
    
    def __init__(self, st=None, inv=None, sampling_interval=60.0, verbose=False, metric='mean', freqmin=0.5, freqmax=15.0, zerophase=False, corners=2, startt=None, endt=None, absolute=True, last_ylist=None, units=None ):
        self.stream = Stream()
        self.metric = metric
        self.corrected = False
        y_list = []


        if isinstance(st, Stream):
            for index,tr in enumerate(st):
                if last_ylist:
                    y = last_ylist[index]
                else:
                    if tr: #tr.stats.channel[2] in 'ENZ' or tr.stats.channel[1:]=='DF': # filter seismic and infrasound channels only
                        # SCAFFOLD: changed line above to add well log data to this analysis
                        print('Processing %s' % tr.id)
                        if inv and tr.stats.units=='Counts': # SCAFFOLD: changed units passed by argument to tr.stats.units. from inv, need to change tr.stats.units elsewhere
                            pre_filt = [freqmin/1.2, freqmin, freqmax, freqmax*1.2]
                            tr.remove_response(output='VEL', inventory=inv, plot=verbose, pre_filt=pre_filt, water_level=60)    
                            self.corrected = True
                            tr.stats['units'] = 'm/s'
                        elif tr.stats.units=='m/s' or tr.stats.units=='Pa':
                            self.corrected = True
                            if absolute: # if not absolute, i.e. keepRaw, then we do not apply any filtering
                                tr.detrend(type='linear')
                                tr.filter('bandpass', freqmin=freqmin, freqmax=freqmax, zerophase=False, corners=corners)                         
                        elif tr.stats.units=='Counts':
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
                    if absolute:
                        y = abs(y)
                y_list.append(y)


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
        #return y_list

    def plot(self, equal_scale=False, type='linear', percentile=None, linestyle='-'):
        st = self.stream.copy()
        for tr in st:
            tr.data = np.where(tr.data==0, np.nan, tr.data)
        if type=='linear':
            linearplot(st, equal_scale=equal_scale, percentile=percentile, linestyle=linestyle)        


    def write(self, SDS_TOP):
        if self.corrected:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'CSAM',self.metric)
        else:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'RSAM',self.metric)           
        RSAMSDSobj = SDS.SDSobj(RSAMSDS_TOP, streamobj=self.stream)
        RSAMSDSobj.write(overwrite=True)

    
    def read(self, startt, endt, SDS_TOP, metric='mean', speed=2, trace_ids=None, corrected=False):
        if corrected:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'CSAM',self.metric)
        else:
            RSAMSDS_TOP = os.path.join(SDS_TOP,'RSAM',self.metric)           
        thisSDSobj = SDS.SDSobj(RSAMSDS_TOP)
        thisSDSobj.read(startt, endt, speed=speed, trace_ids=trace_ids)
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




