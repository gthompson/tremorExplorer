from obspy.clients.nrl import NRL
from obspy.core.inventory import Inventory, Network, Station, Channel, Site
from obspy.core import UTCDateTime

def make_inv(net, sta, loc, chans, datalogger='Centaur', sensor='TCP', Vpp=40, fsamp=100, lat=0.0, lon=0.0, elev=0.0, depth=0.0, sitename='', ondate=UTCDateTime(1970,1,1), offdate=UTCDateTime(2025,12,31)):
    nrl = NRL('http://ds.iris.edu/NRL/')
    if datalogger == 'Centaur':
        if Vpp==40:
            datalogger_keys = ['Nanometrics', 'Centaur', '40 Vpp (1)', 'Off', 'Linear phase', "%d" % fsamp]
        elif Vpp==1:
            datalogger_keys = ['Nanometrics', 'Centaur', '1 Vpp (40)', 'Off', 'Linear phase', "%d" % fsamp]
    elif datalogger == 'RT130':
        datalogger_keys = ['REF TEK', 'RT 130 & 130-SMA', '1', "%d" % fsamp]
    else:
        print(datalogger, ' not recognized')
        print(nrl.dataloggers[datalogger])
    print(datalogger_keys)
 
    if sensor == 'TCP':
        sensor_keys = ['Nanometrics', 'Trillium Compact 120 (Vault, Posthole, OBS)', '754 V/m/s']
    elif sensor == 'L-22':
        sensor_keys = ['Sercel/Mark Products','L-22D','2200 Ohms','10854 Ohms']
    elif sensor == 'Chap':
        sensor_keys = ['Chaparral Physics', '25', 'Low: 0.4 V/Pa']
    else:
        print(sensor, ' not recognized')
        print(nrl.sensors[sensor])
    print(sensor_keys)



    response = nrl.get_response(sensor_keys=sensor_keys, datalogger_keys=datalogger_keys)
    print(response)
    print(response.instrument_sensitivity)
    channels = [] 
    for chan in chans:
        channel = Channel(code=chan,
                      location_code=loc,
                      latitude=lat,
                      longitude=lon,
                      elevation=elev,
                      depth=depth,
                      sample_rate=fsamp,
                      start_date=ondate,
                      end_date=offdate,
                      )
        channel.response = response
        channels.append(channel)
    station = Station(code=sta,
                      latitude=lat,
                      longitude=lon,
                      elevation=elev,
                      creation_date=ondate,
                      site=Site(name=sitename),
                      channels=channels,
                      start_date=ondate,
                      end_date=offdate,
                      )

    network = Network(code=net,
                     stations=[station])
    inventory = Inventory(networks=[network], source="demo")
    return inventory




if __name__ == '__main__':
    inv = make_inv('FL', 'BCHH', '', ['HHZ', 'HHN', 'HHE'], datalogger='Centaur', sensor='TCP', Vpp=40, fsamp=100, sitename='Beach House original', ondate=UTCDateTime(2016,2,24) )
    inv.write("BCHH_original_seismic.sml", format="stationxml", validate=True)
    inv = make_inv('FL', 'BCHH', '', ['HDF'], datalogger='Centaur', sensor='Chap', Vpp=40, fsamp=100, sitename='Beach House Sonic', ondate=UTCDateTime(2017,8,1) )
    inv.write("BCHH_sonic_Chap.sml", format="stationxml", validate=True)
