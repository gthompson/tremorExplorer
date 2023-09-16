# tremorExplorer

tremorExplorer is an aspirational project to develop a Python application for near-real-time visualization and rapid browsing of multi-station spectrograms, RSAM, and reduced displacement plots for one or many volcano-seismic subnetworks. It will also be run in backfill mode to facilitate rapid exploration of a continuous seismic data archive. The application wwill be designed with ease of use in mind, mimicing Pensive. Spectrograms will be instrument-corrected, if instrument response files are available. tremorExplorer will strive to use sensible defaults in all areas while proving an expressive configuration file to permit fine-grained control when needed. 

## Requirements
  * A Python installation with obspy, numpy, matplotlib. We recommend using Anaconda or Miniconda. A yaml-file will be packaged with each released version, containing necessary Python packages and recommended versions.
  * Source of waveform data. tremorExplorer can request data using most options supported by ObsPy's read. For example:
      * the Winston wave server protocol or the Earthworm WaveServerV protocol.
      * a Seedlink server
      * an FDSN server
      * an SDS archive 
      * a SEED or MiniSEED file, which could contain multiple NSLC's and up to 24 hours of data.
      Other data sources can easily be added, e.g. a continuous Seisan or Antelope database.
  * A Web browser. Tested with recent versions of [Firefox](https://www.mozilla.org/firefox/), [Chrome](https://www.google.com/chrome/index.html), [Safari](https://www.apple.com/safari/), and [Internet Exporer](https://windows.microsoft.com/ie).
  * If instrument-corrected spectrograms are desired, instrument responses must be provided in a format the ObsPy can read with the read_inventory command. We recommend using StationXML format for best results.
  
## Installation
tremorExplorer will be distributed as a zip file containing both the application and its required libraries. No further installation will be required.

## Configuration
tremorExplorer looks for its configuration in a file called default.config in the current working directory. Optionally, a different filename may be provided as the last argument on the command line when launching tremorExplorer. An example config called AVO.config is provided. Copy this to default.config using your command line or file manager. 

## Starting tremorExplorer
tremorExplorer can be run in either real-time or back-fill modes. 

### Starting tremorExplorer in real-time mode
In real-time mode tremorExplorer will create a continuous series of plots. Every ten minutes tremorExplorer will wake up to create plots which cover the previous time span and then go to sleep. This will continue until the program is exited. Start tremorExplorer in real-time mode with a command similar to the one below.

    python tremorExplorer.py -c default.config
    
### Starting tremorExplorer in back-fill mode
In back-fill mode, tremorExplorer will create a series of plots for a given timespan, then exit. tremorExplorer can be started in back-fill mode with a command similar to the one below. Times are provided in yyyyMMddHHmm format.

    python tremorExplorer.py -c default.config --startTime 201512011300 --endTime 201512020000

tremorExplorer will not re-create existing plots within the given timespan by default. This can be overridden with the -f flag, which forces overwriting to occur.

## Additional Features enabled by command line options
tremorExplorer contains additional features, which can be optionally turned on by using the --all flag, e.g.
    python tremorExplorer.py --all

This is equivalent to:
    python tremorExplorer.py -c iceweb.config --daily --rsam 7 --dr 7 --drs 7 --alarm 

Individual features can be turned on and modified explicity. These are:

* Daily spectrograms. These will be generated if the --daily switch is added, e.g.
    python tremorExplorer.py --daily

* RSAM data & plots. These will be generated if the --rsam switch is added. RSAM data with a 1-minute sampling interval are calculated by computing the mean absolute value of each 1-minute (non-overlapping) timewindow. If instrument response files exist, seismograms will be instrument corrected to velocity seismograms before RSAM is calculated. Otherwise, RSAM will be "raw" (units will raw digitizer counts). A numerical argument must also be added, to indicate the number of past days to plot reduced displacement for, e.g.  
    python tremorExplorer.py --rsam 7
 will (re-)create a last 7-day RSAM plot every 10 minutes. RSAM data is also saved to daily CSV files. In back-fill mode, RSAM data are computed, but no plots are generated.

* Reduced displacement data and plots. These will be generated if the --dr or --drs switches are added. --dr will correct for geometrical spreading assuming body waves. --drs will assume surface waves. (Note that no correction for attenuation Q is made). Instrument response files must be provided, and seismograms will be instrument corrected to displacement seismograms before a geometrical spreading correction is made to compute reduced displacement. The latter uses the (assumed) source location for each volcano listed in config file. A numerical argument must also be added, to indicate the number of past days to plot reduced displacement for, e.g.  
    python tremorExplorer.py --drs 7
 will (re-)create a last 7-day surface-wave reduced displacement plot every 10 minutes. Reduced displacement data is also saved to daily CSV files. In back-fill mode, reduced displacement data are computed, but no plots are generated.

* Alarm. If the --alarm switch is added, a simple tremor alarm system is run on the data. This automatically enables reduced displacement calculation too. If at least 50% of stations exceed 5 cm^2 of reduced displacement, a level 1 alarm is issued. Further level 1 alarms are then disabled for 1 hour. The same logic applies for a level 2 alarm, except that the threshold is 10 cm^2. For a level 3 alarm, the threshold is 20 cm^2. An alarm.log file is appended to with the volcano, alarm time, alarm level, and reduced displacement level found on eachNSLC listed for that volcano in the config file. Once an alarm level is declared, two consecutive 10-minute timewindows failing to meet the corresponding threshold results in that alarm being cancelled. Once a level 1 alarm is cancelled, the tremor episode is considered over. Alarm level cancellations are also logged in alarm.log.  

* Audio. If the --audio switch is added, audio files are made corresponding to each 10-min spectrogram. These can be played from the spectrogram browser.

## Ideas: 
* I could replicate RSAM bar graphs, but instead of 2.5s, 1-min, 10-min, I could do for each day 1-day, 7-days, 30-days. 
* For alarms, rather than use a threshold I could compare 10-min versus 1-day, 7-day, 30-day. Then alarm level could be product of %ile above 95%ile, and number of minutes. For example, 96%ile for all 10 minutes would be a level 96-95 * 10. 98%ile for 2 minutes (e.g. a regional) would be 98-95 * 2 = 6. If alarm on, an alarm off could be activated by a product less than half of alarm on level. 
* It would be ideal to base everything from spectral data, including RSAM & reduced displacement, band ratios (f_index), peakf, meanf. Alarms too: I could devise event, swarm, tremor, harmonic tremor, and banded tremor alarms (might need to enable 1-s RSAM for event & swarm alarms, and compute nanmax in addition to nanmedian to). Ampmap for tremor could be done from 1-min RSAM. Ampmap for rockfalls could be done from 1-s RSAM. Just forcing a simple 2-D location, ignoring vertical dimension, velocity structure, topography etc. 
* Measuring ellipticity, planarity, linearity etc. could help with wave identification of tremor. Could then correct based on the ratio of body to surface waves indicated. Could also help with location.
* Helicoders could be re-enabled too, but indicating event, swarm, and tremor alarm declarations. 
