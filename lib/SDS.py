######################################################################
##   Extended version of ObsPy sdsclient                            ##
######################################################################

from obspy import Stream, read
import obspy.clients.filesystem.sds
import os
import numpy as np
import pandas as pd

class SDSobj():
    # Call like:
    # myclient = obspyGT.SDS.SDS(SDS_TOP, sds_type='D', format='MSEED')
    def __init__(self, SDS_TOP, sds_type='D', format='MSEED', streamobj=Stream()):
        if not os.path.isdir(SDS_TOP):
            os.makedirs(SDS_TOP, exist_ok=True)    
        self.client = obspy.clients.filesystem.sds.Client(SDS_TOP, sds_type=sds_type, format=format)
        self.stream = streamobj

    # Read SDS archive
    def read(self, startt, endt, skip_low_rate_channels=True, trace_ids=None, speed=1, verbose=True ):
        if not trace_ids:
            #nslc_tuples = sdsclient.get_all_nslc(sds_type='D', datetime=startt) 
            trace_ids = self._sds_get_nonempty_traceids(startt, endt)

        st = Stream()
        for trace_id in trace_ids:
            net, sta, loc, chan = trace_id.split('.')
            if chan[0]=='L' and skip_low_rate_channels:
                print(trace_id,' skipped')
                continue
            if speed==1:
                sdsfiles = self.client._get_filenames(net, sta, loc, chan, startt, endt)
                #print(sdsfiles)
                this_st = Stream()
                for sdsfile in sdsfiles:
                    if os.path.isfile(sdsfile):
                        if verbose:
                            print('st = read("%s")' % sdsfile)
                        that_st = read(sdsfile)
                        that_st.merge(method=1,fill_value=0)
                        #print(sdsfile, that_st)
                        for tr in that_st:
                            this_st.append(tr)  
            elif speed==2:
                this_st = self.client.get_waveforms(net, sta, loc, chan, startt, endt, merge=-1)
            if this_st:
                this_st.trim(startt, endt)              
            for tr in this_st:
                st.append(tr)
        if st:
            st.merge(fill_value=0, method=1)
            self.stream = st
            return 0
        else:
            self.stream = st
            return 1

        self.stream = st

    def _sds_get_nonempty_traceids(self, startday, endday=None, skip_low_rate_channels=True):
        thisday = startday
        trace_ids = []   
        if not endday:
            endday = startday + 86400
        while thisday<endday:
            nslc_tuples = self.client.get_all_nslc(sds_type='D', datetime=thisday) 
            for nslc in nslc_tuples:
                trace_id = '.'.join(nslc)
                if not trace_id in trace_ids:
                    net, sta, loc, chan = nslc
                    if chan[0]=='L' and skip_low_rate_channels:
                        continue
                    if self.client.has_data(net, sta, loc, chan):
                        trace_ids.append(trace_id)  
            thisday = thisday + 86400                    
        return sorted(trace_ids)
 

    def _sds_percent_available_per_day(self, startday, endday, skip_low_rate_channels=True, trace_ids=None, speed=1 ):
        # speed can be 1, 2, or 3. The higher the speed, the less accurate the results.
    
        if not trace_ids:
            trace_ids = self._sds_get_nonempty_traceids(startday, endday)
        if len(trace_ids)==0:
            return
        else:
            print(trace_ids)
    
        lod = []
        thisday = startday
   
        while thisday<endday:
            print(thisday.date) #, ' ',newline=False)
            thisDict = {}
            thisDict['date']=thisday.date
            for trace_id in trace_ids:
                net, sta, loc, chan = trace_id.split('.')
            
                if speed<3: # quite slow but most accurate
                    sdsfile = self.client._get_filename(net, sta, loc, chan, thisday)
                    this_percent = 0
                    if os.path.isfile(sdsfile):
                        st = obspy.read(sdsfile)
                        st.merge()
                        tr = st[0]
                        npts_expected = tr.stats.sampling_rate * 86400
                        if speed==1: # slowest, completely accurate
                            npts_got = np.count_nonzero(~np.isnan(tr.data))
                        elif speed==2: # almost as slow, includes np.isnan as valid data sample   
                            npts_got = tr.stats.npts
                        this_percent = 100 * npts_got/npts_expected

                elif speed==3: # much faster
                    this_percent = 100*self.client.get_availability_percentage(net, sta, loc, chan, thisday, thisday+86400)[0]
                
                thisDict[trace_id] = this_percent
            
            lod.append(thisDict)
            thisday = thisday + 86400
        availabilityDF = pd.DataFrame(lod)
        print(availabilityDF);
        return availabilityDF, trace_ids


    def write(self, overwrite=False):
        #print(self)
        #print(self.stream)
        for tr in self.stream:
            #print(tr)
            sdsfile = self.client._get_filename(tr.stats.network, tr.stats.station, tr.stats.location, tr.stats.channel, tr.stats.starttime, 'D')
            sdsdir = os.path.dirname(sdsfile)
            print(sdsdir)       
            if not os.path.isdir(sdsdir):
                os.makedirs(sdsdir, exist_ok=True)
            if overwrite:
                if os.path.isfile(sdsfile): 
                    print(sdsfile,' already contains data. overwriting')
                else:
                    print(sdsfile,' does not already exist. Writing')
                tr.write(sdsfile, 'mseed')
            else:
                if os.path.isfile(sdsfile): # try to load and merge data from file if it already exists
                    st_before = obspy.read(sdsfile)
                    print(sdsfile,' already contains data')
                    print(st_before)
                    print('trying to merge this new trace:')
                    print(tr)
                    tr_now = tr.copy()
                    st_before.append(tr_now)
                    try:
                        st_before.merge(method=1,fill_value=0)
                        print('merge succeeded')
                    except:
                        print('Could not merge. No new data written.')
                        break
                    print('After merging:')
                    print(st_before)
                    if len(st_before)==1:
                        #print("Just one trace")
                        if st_before[0].stats.sampling_rate >= 1:
                            if tr.stats.sampling_rate >= 1:
                                if st_before[0].stats.npts < tr.stats.npts:
                                    tr.write(sdsfile, 'mseed')
                    else:
                        print('Cannot write Stream with more than 1 trace to a single SDS file')
                else:    
                    print(sdsfile,' does not already exist. Writing')
                    tr.write(sdsfile, 'mseed')


