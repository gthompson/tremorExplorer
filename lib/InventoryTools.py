######################################################################
##  Additional tools for ObsPy Inventory class                      ##
######################################################################

def inventory2traceid(inv, chancode=''):
    trace_ids = list()

    for networkObject in inv:
        if chancode:
            networkObject = networkObject.select(channel=chancode)
        stationObjects = networkObject.stations

        for stationObject in stationObjects:
            channelObjects = stationObject.channels
            for channelObject in channelObjects:
                this_trace_id = networkObject.code + '.' + stationObject.code + '.*.' + channelObject.code
                trace_ids.append(this_trace_id)
    
    return trace_ids


def attach_station_coordinates_from_inventory(inventory, st):
    """ attach_station_coordinates_from_inventory """
    from obspy.core.util import AttribDict
    for tr in st:
        for netw in inventory.networks:
            for sta in netw.stations:
                if tr.stats.station == sta.code and netw.code == tr.stats.network:
                    for cha in sta.channels:
                        if tr.stats.location == cha.location_code:
                            tr.stats.coordinates = AttribDict({
                                'latitude':cha.latitude,
                                'longitude':cha.longitude,
                                'elevation':cha.elevation})
                            #tr.stats.latitude = cha.latitude
                            #tr.stats.longitude = cha.longitude  
                            
                                                      
def attach_distance_to_stream(st, olat, olon):
    import obspy.geodetics
    for tr in st:
        try:
            alat = tr.stats['coordinates']['latitude']
            alon = tr.stats['coordinates']['longitude']
            print(alat, alon, olat, olon)
            distdeg = obspy.geodetics.locations2degrees(olat, olon, alat, alon)
            distkm = obspy.geodetics.degrees2kilometers(distdeg)
            tr.stats['distance'] =  distkm * 1000
        except Exception as e:
            print(e)
            print('cannot compute distance for %s' % tr.id)

def create_trace_inventory(tr, netname='', sitename='', net_ondate=None, \
                           sta_ondate=None, lat=0.0, lon=0.0, elev=0.0, depth=0.0, azimuth=0.0, dip=-90.0, stationXml=None):
    from obspy.core.inventory import Inventory, Network, Station, Channel, Site
    from obspy.clients.nrl import NRL    
    inv = Inventory(networks=[], source='Glenn Thompson')
    if not sta_ondate:
        net_ondate = tr.stats.starttime
    if not sta_ondate:
        sta_ondate = tr.stats.starttime        
    net = Network(
        # This is the network code according to the SEED standard.
        code=tr.stats.network,
        # A list of stations. We'll add one later.
        stations=[],
        description=netname,
        # Start-and end dates are optional.
        start_date=net_ondate)

    sta = Station(
        # This is the station code according to the SEED standard.
        code=tr.stats.station,
        latitude=lat,
        longitude=lon,
        elevation=elev,
        creation_date=sta_ondate, 
        site=Site(name=sitename))

    cha = Channel(
        # This is the channel code according to the SEED standard.
        code=tr.stats.channel,
        # This is the location code according to the SEED standard.
        location_code=tr.stats.location,
        # Note that these coordinates can differ from the station coordinates.
        latitude=lat,
        longitude=lon,
        elevation=elev,
        depth=depth,
        azimuth=azimuth,
        dip=dip,
        sample_rate=tr.stats.sampling_rate)

    # By default this accesses the NRL online. Offline copies of the NRL can
    # also be used instead
    nrl = NRL()
    # The contents of the NRL can be explored interactively in a Python prompt,
    # see API documentation of NRL submodule:
    # http://docs.obspy.org/packages/obspy.clients.nrl.html
    # Here we assume that the end point of data logger and sensor are already
    # known:
    response = nrl.get_response( # doctest: +SKIP
        sensor_keys=['Streckeisen', 'STS-1', '360 seconds'],
        datalogger_keys=['REF TEK', 'RT 130 & 130-SMA', '1', '200'])


    # Now tie it all together.
    cha.response = response
    sta.channels.append(cha)
    net.stations.append(sta)
    inv.networks.append(net)
    
    # And finally write it to a StationXML file. We also force a validation against
    # the StationXML schema to ensure it produces a valid StationXML file.
    #
    # Note that it is also possible to serialize to any of the other inventory
    # output formats ObsPy supports.
    if stationXml:
        print('Writing inventory to %s' % stationXml)
        inv.write(stationXml, format="stationxml", validate=True)    
    return inv


def _merge_channels(chan1, chan, channel_codes):
    index2 = channel_codes.index(chan.code)
    print('Want to merge channel:')
    print(chan)
    print('into:')
    print(chan1[index2])
    print(chan1[index2].startDate)

    
def _add_channel(chan1, chan):
    # add as new channel
    print('Adding new channel %s' % chan.code)
    chan1.append(chan)  
    
def _merge_stations(sta1, sta, station_codes):
    index = station_codes.index(sta.code)
    print('Merging station')  
    for chan in sta.channels:
        channel_codes = [chan.code for chan in sta1[index].channels]
        if chan.code in channel_codes: 
            #merge_channels(sta1[index].channels, chan, channel_codes)
            _add_channel(sta1[index].channels, chan)
        else: # add as new channel
            _add_channel(sta1[index].channels, chan)           
            
def _add_station(sta1, sta):
    # add as new station
    print('Adding new station %s' % sta.code)
    sta1.append(sta)            
            
def merge_inventories(inv1, inv2):
    netcodes1 = [this_net.code for this_net in inv1.networks]
    for net2 in inv2.networks:
        if net2.code in netcodes1:
            netpos = netcodes1.index(net2.code)
            for sta in net2.stations:
                if inv1.networks[netpos].stations:
                    station_codes = [sta.code for sta in inv1.networks[netpos].stations]
                    if sta.code in station_codes: 
                        _merge_stations(inv1.networks[netpos].stations, sta, station_codes)
                    else:
                        _add_station(inv1.networks[netpos].stations, sta)
                else:
                    _add_station(inv1.networks[netpos].stations, sta)            
        else: # this network code from inv2 does not exist in inv1
            inv1.networks.append(net2)
            netpos = -1
            
            
'''        
    for sta in inv2.networks[0].stations:
        if inv1.networks[0].stations:
            station_codes = [sta.code for sta in inv1.networks[0].stations]
            if sta.code in station_codes: 
                _merge_stations(inv1.networks[0].stations, sta, station_codes)
            else:
                _add_station(inv1.networks[0].stations, sta)
        else:
            _add_station(inv1.networks[0].stations, sta)  
'''