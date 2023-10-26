<?xml version='1.0' encoding='UTF-8'?>
<FDSNStationXML xmlns="http://www.fdsn.org/xml/station/1" schemaVersion="1.1">
  <Source>demo</Source>
  <Module>ObsPy 1.3.0</Module>
  <ModuleURI>https://www.obspy.org</ModuleURI>
  <Created>2023-10-23T20:30:30.621615Z</Created>
  <Network code="FL">
    <Station code="BCHH" startDate="2016-02-24T00:00:00.000000Z" endDate="2025-12-31T00:00:00.000000Z">
      <Latitude unit="DEGREES">0.0</Latitude>
      <Longitude unit="DEGREES">0.0</Longitude>
      <Elevation unit="METERS">0.0</Elevation>
      <Site>
        <Name>Beach House original</Name>
      </Site>
      <CreationDate>2016-02-24T00:00:00.000000Z</CreationDate>
      <Channel code="HHZ" startDate="2016-02-24T00:00:00.000000Z" endDate="2025-12-31T00:00:00.000000Z" locationCode="">
        <Latitude unit="DEGREES">0.0</Latitude>
        <Longitude unit="DEGREES">0.0</Longitude>
        <Elevation unit="METERS">0.0</Elevation>
        <Depth unit="METERS">0.0</Depth>
        <SampleRate>100.0</SampleRate>
        <Response>
          <InstrumentSensitivity>
            <Value>301720003.7617996</Value>
            <Frequency>1.0</Frequency>
            <InputUnits>
              <Name>M/S</Name>
              <Description>Velocity in Meters per Second</Description>
            </InputUnits>
            <OutputUnits>
              <Name>COUNTS</Name>
              <Description>Digital Counts</Description>
            </OutputUnits>
          </InstrumentSensitivity>
          <Stage number="1">
            <PolesZeros>
              <InputUnits>
                <Name>M/S</Name>
                <Description>Velocity in Meters per Second</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>4.344928e+17</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
              <Zero number="0">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="1">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="2">
                <Real minusError="-392.0" plusError="-392.0">-392.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="3">
                <Real minusError="-1960.0" plusError="-1960.0">-1960.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="4">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="1740.0" plusError="1740.0">1740.0</Imaginary>
              </Zero>
              <Zero number="5">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="-1740.0" plusError="-1740.0">-1740.0</Imaginary>
              </Zero>
              <Pole number="0">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="0.03702" plusError="0.03702">0.03702</Imaginary>
              </Pole>
              <Pole number="1">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="-0.03702" plusError="-0.03702">-0.03702</Imaginary>
              </Pole>
              <Pole number="2">
                <Real minusError="-343.0" plusError="-343.0">-343.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="3">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="467.0" plusError="467.0">467.0</Imaginary>
              </Pole>
              <Pole number="4">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="-467.0" plusError="-467.0">-467.0</Imaginary>
              </Pole>
              <Pole number="5">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="1522.0" plusError="1522.0">1522.0</Imaginary>
              </Pole>
              <Pole number="6">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="-1522.0" plusError="-1522.0">-1522.0</Imaginary>
              </Pole>
              <Pole number="7">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="4700.0" plusError="4700.0">4700.0</Imaginary>
              </Pole>
              <Pole number="8">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="-4700.0" plusError="-4700.0">-4700.0</Imaginary>
              </Pole>
              <Pole number="9">
                <Real minusError="-6900.0" plusError="-6900.0">-6900.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="10">
                <Real minusError="-15000.0" plusError="-15000.0">-15000.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
            </PolesZeros>
            <StageGain>
              <Value>754.3</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="2">
            <PolesZeros>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>1.0</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
            </PolesZeros>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="3">
            <Coefficients>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>1.0</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>1</Factor>
              <Offset>0</Offset>
              <Delay>0.0</Delay>
              <Correction>0.0</Correction>
            </Decimation>
            <StageGain>
              <Value>400000.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="4">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-4.047908e-10</Numerator>
              <Numerator>-1.390291e-10</Numerator>
              <Numerator>6.728001e-10</Numerator>
              <Numerator>2.757972e-09</Numerator>
              <Numerator>7.546507e-09</Numerator>
              <Numerator>1.766681e-08</Numerator>
              <Numerator>3.769363e-08</Numerator>
              <Numerator>7.523132e-08</Numerator>
              <Numerator>1.424254e-07</Numerator>
              <Numerator>2.57999e-07</Numerator>
              <Numerator>4.499037e-07</Numerator>
              <Numerator>7.586555e-07</Numerator>
              <Numerator>1.241386e-06</Numerator>
              <Numerator>1.97658e-06</Numerator>
              <Numerator>3.069389e-06</Numerator>
              <Numerator>4.657284e-06</Numerator>
              <Numerator>6.915693e-06</Numerator>
              <Numerator>1.00631e-05</Numerator>
              <Numerator>1.436487e-05</Numerator>
              <Numerator>2.013499e-05</Numerator>
              <Numerator>2.773459e-05</Numerator>
              <Numerator>3.756609e-05</Numerator>
              <Numerator>5.006174e-05</Numerator>
              <Numerator>6.566517e-05</Numerator>
              <Numerator>8.480489e-05</Numerator>
              <Numerator>0.0001078587</Numerator>
              <Numerator>0.0001351084</Numerator>
              <Numerator>0.0001666851</Numerator>
              <Numerator>0.0002025053</Numerator>
              <Numerator>0.0002421999</Numerator>
              <Numerator>0.000285038</Numerator>
              <Numerator>0.0003298504</Numerator>
              <Numerator>0.000374956</Numerator>
              <Numerator>0.0004180986</Numerator>
              <Numerator>0.0004564003</Numerator>
              <Numerator>0.0004863386</Numerator>
              <Numerator>0.0005037566</Numerator>
              <Numerator>0.0005039131</Numerator>
              <Numerator>0.0004815801</Numerator>
              <Numerator>0.0004311946</Numerator>
              <Numerator>0.000347068</Numerator>
              <Numerator>0.0002236552</Numerator>
              <Numerator>5.588177e-05</Numerator>
              <Numerator>-0.0001604755</Numerator>
              <Numerator>-0.0004283654</Numerator>
              <Numerator>-0.0007490084</Numerator>
              <Numerator>-0.001121432</Numerator>
              <Numerator>-0.001542013</Numerator>
              <Numerator>-0.002004062</Numerator>
              <Numerator>-0.002497462</Numerator>
              <Numerator>-0.003008406</Numerator>
              <Numerator>-0.00351925</Numerator>
              <Numerator>-0.004008517</Numerator>
              <Numerator>-0.00445107</Numerator>
              <Numerator>-0.004818468</Numerator>
              <Numerator>-0.005079526</Numerator>
              <Numerator>-0.005201073</Numerator>
              <Numerator>-0.005148892</Numerator>
              <Numerator>-0.004888844</Numerator>
              <Numerator>-0.004388128</Numerator>
              <Numerator>-0.003616642</Numerator>
              <Numerator>-0.002548397</Numerator>
              <Numerator>-0.00116293</Numerator>
              <Numerator>0.0005533497</Numerator>
              <Numerator>0.002605953</Numerator>
              <Numerator>0.004991292</Numerator>
              <Numerator>0.007695918</Numerator>
              <Numerator>0.01069608</Numerator>
              <Numerator>0.01395761</Numerator>
              <Numerator>0.01743625</Numerator>
              <Numerator>0.02107831</Numerator>
              <Numerator>0.02482173</Numerator>
              <Numerator>0.02859758</Numerator>
              <Numerator>0.03233183</Numerator>
              <Numerator>0.0359474</Numerator>
              <Numerator>0.03936644</Numerator>
              <Numerator>0.04251273</Numerator>
              <Numerator>0.04531409</Numerator>
              <Numerator>0.04770474</Numerator>
              <Numerator>0.04962748</Numerator>
              <Numerator>0.05103565</Numerator>
              <Numerator>0.05189471</Numerator>
              <Numerator>0.05218345</Numerator>
              <Numerator>0.05189471</Numerator>
              <Numerator>0.05103565</Numerator>
              <Numerator>0.04962748</Numerator>
              <Numerator>0.04770474</Numerator>
              <Numerator>0.04531409</Numerator>
              <Numerator>0.04251273</Numerator>
              <Numerator>0.03936644</Numerator>
              <Numerator>0.0359474</Numerator>
              <Numerator>0.03233183</Numerator>
              <Numerator>0.02859758</Numerator>
              <Numerator>0.02482173</Numerator>
              <Numerator>0.02107831</Numerator>
              <Numerator>0.01743625</Numerator>
              <Numerator>0.01395761</Numerator>
              <Numerator>0.01069608</Numerator>
              <Numerator>0.007695918</Numerator>
              <Numerator>0.004991292</Numerator>
              <Numerator>0.002605953</Numerator>
              <Numerator>0.0005533497</Numerator>
              <Numerator>-0.00116293</Numerator>
              <Numerator>-0.002548397</Numerator>
              <Numerator>-0.003616642</Numerator>
              <Numerator>-0.004388128</Numerator>
              <Numerator>-0.004888844</Numerator>
              <Numerator>-0.005148892</Numerator>
              <Numerator>-0.005201073</Numerator>
              <Numerator>-0.005079526</Numerator>
              <Numerator>-0.004818468</Numerator>
              <Numerator>-0.00445107</Numerator>
              <Numerator>-0.004008517</Numerator>
              <Numerator>-0.00351925</Numerator>
              <Numerator>-0.003008406</Numerator>
              <Numerator>-0.002497462</Numerator>
              <Numerator>-0.002004062</Numerator>
              <Numerator>-0.001542013</Numerator>
              <Numerator>-0.001121432</Numerator>
              <Numerator>-0.0007490084</Numerator>
              <Numerator>-0.0004283654</Numerator>
              <Numerator>-0.0001604755</Numerator>
              <Numerator>5.588177e-05</Numerator>
              <Numerator>0.0002236552</Numerator>
              <Numerator>0.000347068</Numerator>
              <Numerator>0.0004311946</Numerator>
              <Numerator>0.0004815801</Numerator>
              <Numerator>0.0005039131</Numerator>
              <Numerator>0.0005037566</Numerator>
              <Numerator>0.0004863386</Numerator>
              <Numerator>0.0004564003</Numerator>
              <Numerator>0.0004180986</Numerator>
              <Numerator>0.000374956</Numerator>
              <Numerator>0.0003298504</Numerator>
              <Numerator>0.000285038</Numerator>
              <Numerator>0.0002421999</Numerator>
              <Numerator>0.0002025053</Numerator>
              <Numerator>0.0001666851</Numerator>
              <Numerator>0.0001351084</Numerator>
              <Numerator>0.0001078587</Numerator>
              <Numerator>8.480489e-05</Numerator>
              <Numerator>6.566517e-05</Numerator>
              <Numerator>5.006174e-05</Numerator>
              <Numerator>3.756609e-05</Numerator>
              <Numerator>2.773459e-05</Numerator>
              <Numerator>2.013499e-05</Numerator>
              <Numerator>1.436487e-05</Numerator>
              <Numerator>1.00631e-05</Numerator>
              <Numerator>6.915693e-06</Numerator>
              <Numerator>4.657284e-06</Numerator>
              <Numerator>3.069389e-06</Numerator>
              <Numerator>1.97658e-06</Numerator>
              <Numerator>1.241386e-06</Numerator>
              <Numerator>7.586555e-07</Numerator>
              <Numerator>4.499037e-07</Numerator>
              <Numerator>2.57999e-07</Numerator>
              <Numerator>1.424254e-07</Numerator>
              <Numerator>7.523132e-08</Numerator>
              <Numerator>3.769363e-08</Numerator>
              <Numerator>1.766681e-08</Numerator>
              <Numerator>7.546507e-09</Numerator>
              <Numerator>2.757972e-09</Numerator>
              <Numerator>6.728001e-10</Numerator>
              <Numerator>-1.390291e-10</Numerator>
              <Numerator>-4.047908e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>15</Factor>
              <Offset>0</Offset>
              <Delay>0.002733333</Delay>
              <Correction>0.002733333</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="5">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>8.46923e-10</Numerator>
              <Numerator>2.27422e-09</Numerator>
              <Numerator>4.538951e-09</Numerator>
              <Numerator>6.873791e-09</Numerator>
              <Numerator>7.10904e-09</Numerator>
              <Numerator>7.627841e-10</Numerator>
              <Numerator>-1.98301e-08</Numerator>
              <Numerator>-6.609942e-08</Numerator>
              <Numerator>-1.531138e-07</Numerator>
              <Numerator>-2.982495e-07</Numerator>
              <Numerator>-5.181519e-07</Numerator>
              <Numerator>-8.236356e-07</Numerator>
              <Numerator>-1.212476e-06</Numerator>
              <Numerator>-1.660555e-06</Numerator>
              <Numerator>-2.112474e-06</Numerator>
              <Numerator>-2.473531e-06</Numerator>
              <Numerator>-2.605619e-06</Numerator>
              <Numerator>-2.330134e-06</Numerator>
              <Numerator>-1.44098e-06</Numerator>
              <Numerator>2.698043e-07</Numerator>
              <Numerator>2.972714e-06</Numerator>
              <Numerator>6.748858e-06</Numerator>
              <Numerator>1.152962e-05</Numerator>
              <Numerator>1.703543e-05</Numerator>
              <Numerator>2.272479e-05</Numerator>
              <Numerator>2.776698e-05</Numerator>
              <Numerator>3.105368e-05</Numerator>
              <Numerator>3.126302e-05</Numerator>
              <Numerator>2.698613e-05</Numerator>
              <Numerator>1.691886e-05</Numerator>
              <Numerator>1.111765e-07</Numerator>
              <Numerator>-2.374559e-05</Numerator>
              <Numerator>-5.402672e-05</Numerator>
              <Numerator>-8.892268e-05</Numerator>
              <Numerator>-0.0001252819</Numerator>
              <Numerator>-0.0001586044</Numerator>
              <Numerator>-0.0001832359</Numerator>
              <Numerator>-0.000192798</Numerator>
              <Numerator>-0.0001808636</Numerator>
              <Numerator>-0.0001418502</Numerator>
              <Numerator>-7.206699e-05</Numerator>
              <Numerator>2.919376e-05</Numerator>
              <Numerator>0.0001586655</Numerator>
              <Numerator>0.0003083858</Numerator>
              <Numerator>0.0004654217</Numerator>
              <Numerator>0.0006121983</Numerator>
              <Numerator>0.0007275471</Numerator>
              <Numerator>0.0007885116</Numerator>
              <Numerator>0.0007728578</Numerator>
              <Numerator>0.000662123</Numerator>
              <Numerator>0.000444926</Numerator>
              <Numerator>0.0001201614</Numerator>
              <Numerator>-0.0003003695</Numerator>
              <Numerator>-0.0007903605</Numerator>
              <Numerator>-0.001308874</Numerator>
              <Numerator>-0.00180202</Numerator>
              <Numerator>-0.002206618</Numerator>
              <Numerator>-0.00245579</Numerator>
              <Numerator>-0.002486192</Numerator>
              <Numerator>-0.002246312</Numerator>
              <Numerator>-0.001705031</Numerator>
              <Numerator>-0.0008594633</Numerator>
              <Numerator>0.0002590112</Numerator>
              <Numerator>0.001581566</Numerator>
              <Numerator>0.003002498</Numerator>
              <Numerator>0.004384142</Numerator>
              <Numerator>0.005566316</Numerator>
              <Numerator>0.006380002</Numerator>
              <Numerator>0.006664402</Numerator>
              <Numerator>0.006286043</Numerator>
              <Numerator>0.005158141</Numerator>
              <Numerator>0.003258199</Numerator>
              <Numerator>0.0006416821</Numerator>
              <Numerator>-0.002550179</Numerator>
              <Numerator>-0.006090065</Numerator>
              <Numerator>-0.009672703</Numerator>
              <Numerator>-0.01293168</Numerator>
              <Numerator>-0.01546425</Numerator>
              <Numerator>-0.01686256</Numerator>
              <Numerator>-0.01674898</Numerator>
              <Numerator>-0.01481246</Numerator>
              <Numerator>-0.01084255</Numerator>
              <Numerator>-0.004757783</Numerator>
              <Numerator>0.003374886</Numerator>
              <Numerator>0.01333183</Numerator>
              <Numerator>0.02473738</Numerator>
              <Numerator>0.03708165</Numerator>
              <Numerator>0.0497507</Numerator>
              <Numerator>0.06206696</Numerator>
              <Numerator>0.07333685</Numerator>
              <Numerator>0.08290152</Numerator>
              <Numerator>0.0901866</Numerator>
              <Numerator>0.09474635</Numerator>
              <Numerator>0.09629848</Numerator>
              <Numerator>0.09474635</Numerator>
              <Numerator>0.0901866</Numerator>
              <Numerator>0.08290152</Numerator>
              <Numerator>0.07333685</Numerator>
              <Numerator>0.06206696</Numerator>
              <Numerator>0.0497507</Numerator>
              <Numerator>0.03708165</Numerator>
              <Numerator>0.02473738</Numerator>
              <Numerator>0.01333183</Numerator>
              <Numerator>0.003374886</Numerator>
              <Numerator>-0.004757783</Numerator>
              <Numerator>-0.01084255</Numerator>
              <Numerator>-0.01481246</Numerator>
              <Numerator>-0.01674898</Numerator>
              <Numerator>-0.01686256</Numerator>
              <Numerator>-0.01546425</Numerator>
              <Numerator>-0.01293168</Numerator>
              <Numerator>-0.009672703</Numerator>
              <Numerator>-0.006090065</Numerator>
              <Numerator>-0.002550179</Numerator>
              <Numerator>0.0006416821</Numerator>
              <Numerator>0.003258199</Numerator>
              <Numerator>0.005158141</Numerator>
              <Numerator>0.006286043</Numerator>
              <Numerator>0.006664402</Numerator>
              <Numerator>0.006380002</Numerator>
              <Numerator>0.005566316</Numerator>
              <Numerator>0.004384142</Numerator>
              <Numerator>0.003002498</Numerator>
              <Numerator>0.001581566</Numerator>
              <Numerator>0.0002590112</Numerator>
              <Numerator>-0.0008594633</Numerator>
              <Numerator>-0.001705031</Numerator>
              <Numerator>-0.002246312</Numerator>
              <Numerator>-0.002486192</Numerator>
              <Numerator>-0.00245579</Numerator>
              <Numerator>-0.002206618</Numerator>
              <Numerator>-0.00180202</Numerator>
              <Numerator>-0.001308874</Numerator>
              <Numerator>-0.0007903605</Numerator>
              <Numerator>-0.0003003695</Numerator>
              <Numerator>0.0001201614</Numerator>
              <Numerator>0.000444926</Numerator>
              <Numerator>0.000662123</Numerator>
              <Numerator>0.0007728578</Numerator>
              <Numerator>0.0007885116</Numerator>
              <Numerator>0.0007275471</Numerator>
              <Numerator>0.0006121983</Numerator>
              <Numerator>0.0004654217</Numerator>
              <Numerator>0.0003083858</Numerator>
              <Numerator>0.0001586655</Numerator>
              <Numerator>2.919376e-05</Numerator>
              <Numerator>-7.206699e-05</Numerator>
              <Numerator>-0.0001418502</Numerator>
              <Numerator>-0.0001808636</Numerator>
              <Numerator>-0.000192798</Numerator>
              <Numerator>-0.0001832359</Numerator>
              <Numerator>-0.0001586044</Numerator>
              <Numerator>-0.0001252819</Numerator>
              <Numerator>-8.892268e-05</Numerator>
              <Numerator>-5.402672e-05</Numerator>
              <Numerator>-2.374559e-05</Numerator>
              <Numerator>1.111765e-07</Numerator>
              <Numerator>1.691886e-05</Numerator>
              <Numerator>2.698613e-05</Numerator>
              <Numerator>3.126302e-05</Numerator>
              <Numerator>3.105368e-05</Numerator>
              <Numerator>2.776698e-05</Numerator>
              <Numerator>2.272479e-05</Numerator>
              <Numerator>1.703543e-05</Numerator>
              <Numerator>1.152962e-05</Numerator>
              <Numerator>6.748858e-06</Numerator>
              <Numerator>2.972714e-06</Numerator>
              <Numerator>2.698043e-07</Numerator>
              <Numerator>-1.44098e-06</Numerator>
              <Numerator>-2.330134e-06</Numerator>
              <Numerator>-2.605619e-06</Numerator>
              <Numerator>-2.473531e-06</Numerator>
              <Numerator>-2.112474e-06</Numerator>
              <Numerator>-1.660555e-06</Numerator>
              <Numerator>-1.212476e-06</Numerator>
              <Numerator>-8.236356e-07</Numerator>
              <Numerator>-5.181519e-07</Numerator>
              <Numerator>-2.982495e-07</Numerator>
              <Numerator>-1.531138e-07</Numerator>
              <Numerator>-6.609942e-08</Numerator>
              <Numerator>-1.98301e-08</Numerator>
              <Numerator>7.627841e-10</Numerator>
              <Numerator>7.10904e-09</Numerator>
              <Numerator>6.873791e-09</Numerator>
              <Numerator>4.538951e-09</Numerator>
              <Numerator>2.27422e-09</Numerator>
              <Numerator>8.46923e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">2000.0</InputSampleRate>
              <Factor>10</Factor>
              <Offset>0</Offset>
              <Delay>0.0465</Delay>
              <Correction>0.0465</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="6">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-2.487704e-10</Numerator>
              <Numerator>4.73744e-09</Numerator>
              <Numerator>1.240319e-08</Numerator>
              <Numerator>2.18423e-09</Numerator>
              <Numerator>-2.973504e-08</Numerator>
              <Numerator>-2.774098e-08</Numerator>
              <Numerator>4.823501e-08</Numerator>
              <Numerator>9.04852e-08</Numerator>
              <Numerator>-4.377202e-08</Numerator>
              <Numerator>-2.029251e-07</Numerator>
              <Numerator>-2.93251e-08</Numerator>
              <Numerator>3.576771e-07</Numerator>
              <Numerator>2.380756e-07</Numerator>
              <Numerator>-5.050541e-07</Numerator>
              <Numerator>-6.566606e-07</Numerator>
              <Numerator>5.295136e-07</Numerator>
              <Numerator>1.333027e-06</Numerator>
              <Numerator>-2.353909e-07</Numerator>
              <Numerator>-2.234558e-06</Numerator>
              <Numerator>-6.431887e-07</Numerator>
              <Numerator>3.178848e-06</Numerator>
              <Numerator>2.391894e-06</Numerator>
              <Numerator>-3.766426e-06</Numerator>
              <Numerator>-5.213131e-06</Numerator>
              <Numerator>3.343879e-06</Numerator>
              <Numerator>9.069842e-06</Numerator>
              <Numerator>-1.034203e-06</Numerator>
              <Numerator>-1.349476e-05</Numerator>
              <Numerator>-4.128203e-06</Numerator>
              <Numerator>1.740814e-05</Numerator>
              <Numerator>1.293247e-05</Numerator>
              <Numerator>-1.901116e-05</Numerator>
              <Numerator>-2.55982e-05</Numerator>
              <Numerator>1.583847e-05</Numerator>
              <Numerator>4.129854e-05</Numerator>
              <Numerator>-5.051362e-06</Numerator>
              <Numerator>-5.769434e-05</Numerator>
              <Numerator>-1.597343e-05</Numerator>
              <Numerator>7.06232e-05</Numerator>
              <Numerator>4.876212e-05</Numerator>
              <Numerator>-7.411825e-05</Numerator>
              <Numerator>-9.265601e-05</Numerator>
              <Numerator>6.092806e-05</Numerator>
              <Numerator>0.0001437042</Numerator>
              <Numerator>-2.365713e-05</Numerator>
              <Numerator>-0.0001938177</Numerator>
              <Numerator>-4.346068e-05</Numerator>
              <Numerator>0.0002305286</Numerator>
              <Numerator>0.0001422997</Numerator>
              <Numerator>-0.0002376966</Numerator>
              <Numerator>-0.0002684195</Numerator>
              <Numerator>0.00019742</Numerator>
              <Numerator>0.0004089862</Numerator>
              <Numerator>-9.322642e-05</Numerator>
              <Numerator>-0.0005416667</Numerator>
              <Numerator>-8.56506e-05</Numerator>
              <Numerator>0.0006351459</Numerator>
              <Numerator>0.0003394235</Numerator>
              <Numerator>-0.0006517938</Numerator>
              <Numerator>-0.0006531623</Numerator>
              <Numerator>0.000552734</Numerator>
              <Numerator>0.0009935334</Numerator>
              <Numerator>-0.000305133</Numerator>
              <Numerator>-0.00130802</Numerator>
              <Numerator>-0.0001089867</Numerator>
              <Numerator>0.001527642</Numerator>
              <Numerator>0.0006836461</Numerator>
              <Numerator>-0.001573808</Numerator>
              <Numerator>-0.00138119</Numerator>
              <Numerator>0.001369316</Numerator>
              <Numerator>0.002127841</Numerator>
              <Numerator>-0.0008527391</Numerator>
              <Numerator>-0.002814326</Numerator>
              <Numerator>-5.435981e-06</Numerator>
              <Numerator>0.003302926</Numerator>
              <Numerator>0.001187235</Numerator>
              <Numerator>-0.003441493</Numerator>
              <Numerator>-0.002615018</Numerator>
              <Numerator>0.003083861</Numerator>
              <Numerator>0.004145541</Numerator>
              <Numerator>-0.002114933</Numerator>
              <Numerator>-0.005572669</Numerator>
              <Numerator>0.0004775432</Numerator>
              <Numerator>0.006640171</Numerator>
              <Numerator>0.001802538</Numerator>
              <Numerator>-0.00706464</Numerator>
              <Numerator>-0.004597381</Numerator>
              <Numerator>0.00656694</Numerator>
              <Numerator>0.007666904</Numerator>
              <Numerator>-0.00490895</Numerator>
              <Numerator>-0.01066029</Numerator>
              <Numerator>0.001931064</Numerator>
              <Numerator>0.01312888</Numerator>
              <Numerator>0.002414871</Numerator>
              <Numerator>-0.01454758</Numerator>
              <Numerator>-0.008042475</Numerator>
              <Numerator>0.01433728</Numerator>
              <Numerator>0.01472206</Numerator>
              <Numerator>-0.01187359</Numerator>
              <Numerator>-0.02208895</Numerator>
              <Numerator>0.00645106</Numerator>
              <Numerator>0.0296694</Numerator>
              <Numerator>0.002871719</Numerator>
              <Numerator>-0.03692219</Numerator>
              <Numerator>-0.01777635</Numerator>
              <Numerator>0.04329151</Numerator>
              <Numerator>0.04248361</Numerator>
              <Numerator>-0.04826485</Numerator>
              <Numerator>-0.09280869</Numerator>
              <Numerator>0.05142858</Numerator>
              <Numerator>0.3137774</Numerator>
              <Numerator>0.4474858</Numerator>
              <Numerator>0.3137774</Numerator>
              <Numerator>0.05142858</Numerator>
              <Numerator>-0.09280869</Numerator>
              <Numerator>-0.04826485</Numerator>
              <Numerator>0.04248361</Numerator>
              <Numerator>0.04329151</Numerator>
              <Numerator>-0.01777635</Numerator>
              <Numerator>-0.03692219</Numerator>
              <Numerator>0.002871719</Numerator>
              <Numerator>0.0296694</Numerator>
              <Numerator>0.00645106</Numerator>
              <Numerator>-0.02208895</Numerator>
              <Numerator>-0.01187359</Numerator>
              <Numerator>0.01472206</Numerator>
              <Numerator>0.01433728</Numerator>
              <Numerator>-0.008042475</Numerator>
              <Numerator>-0.01454758</Numerator>
              <Numerator>0.002414871</Numerator>
              <Numerator>0.01312888</Numerator>
              <Numerator>0.001931064</Numerator>
              <Numerator>-0.01066029</Numerator>
              <Numerator>-0.00490895</Numerator>
              <Numerator>0.007666904</Numerator>
              <Numerator>0.00656694</Numerator>
              <Numerator>-0.004597381</Numerator>
              <Numerator>-0.00706464</Numerator>
              <Numerator>0.001802538</Numerator>
              <Numerator>0.006640171</Numerator>
              <Numerator>0.0004775432</Numerator>
              <Numerator>-0.005572669</Numerator>
              <Numerator>-0.002114933</Numerator>
              <Numerator>0.004145541</Numerator>
              <Numerator>0.003083861</Numerator>
              <Numerator>-0.002615018</Numerator>
              <Numerator>-0.003441493</Numerator>
              <Numerator>0.001187235</Numerator>
              <Numerator>0.003302926</Numerator>
              <Numerator>-5.435981e-06</Numerator>
              <Numerator>-0.002814326</Numerator>
              <Numerator>-0.0008527391</Numerator>
              <Numerator>0.002127841</Numerator>
              <Numerator>0.001369316</Numerator>
              <Numerator>-0.00138119</Numerator>
              <Numerator>-0.001573808</Numerator>
              <Numerator>0.0006836461</Numerator>
              <Numerator>0.001527642</Numerator>
              <Numerator>-0.0001089867</Numerator>
              <Numerator>-0.00130802</Numerator>
              <Numerator>-0.000305133</Numerator>
              <Numerator>0.0009935334</Numerator>
              <Numerator>0.000552734</Numerator>
              <Numerator>-0.0006531623</Numerator>
              <Numerator>-0.0006517938</Numerator>
              <Numerator>0.0003394235</Numerator>
              <Numerator>0.0006351459</Numerator>
              <Numerator>-8.56506e-05</Numerator>
              <Numerator>-0.0005416667</Numerator>
              <Numerator>-9.322642e-05</Numerator>
              <Numerator>0.0004089862</Numerator>
              <Numerator>0.00019742</Numerator>
              <Numerator>-0.0002684195</Numerator>
              <Numerator>-0.0002376966</Numerator>
              <Numerator>0.0001422997</Numerator>
              <Numerator>0.0002305286</Numerator>
              <Numerator>-4.346068e-05</Numerator>
              <Numerator>-0.0001938177</Numerator>
              <Numerator>-2.365713e-05</Numerator>
              <Numerator>0.0001437042</Numerator>
              <Numerator>6.092806e-05</Numerator>
              <Numerator>-9.265601e-05</Numerator>
              <Numerator>-7.411825e-05</Numerator>
              <Numerator>4.876212e-05</Numerator>
              <Numerator>7.06232e-05</Numerator>
              <Numerator>-1.597343e-05</Numerator>
              <Numerator>-5.769434e-05</Numerator>
              <Numerator>-5.051362e-06</Numerator>
              <Numerator>4.129854e-05</Numerator>
              <Numerator>1.583847e-05</Numerator>
              <Numerator>-2.55982e-05</Numerator>
              <Numerator>-1.901116e-05</Numerator>
              <Numerator>1.293247e-05</Numerator>
              <Numerator>1.740814e-05</Numerator>
              <Numerator>-4.128203e-06</Numerator>
              <Numerator>-1.349476e-05</Numerator>
              <Numerator>-1.034203e-06</Numerator>
              <Numerator>9.069842e-06</Numerator>
              <Numerator>3.343879e-06</Numerator>
              <Numerator>-5.213131e-06</Numerator>
              <Numerator>-3.766426e-06</Numerator>
              <Numerator>2.391894e-06</Numerator>
              <Numerator>3.178848e-06</Numerator>
              <Numerator>-6.431887e-07</Numerator>
              <Numerator>-2.234558e-06</Numerator>
              <Numerator>-2.353909e-07</Numerator>
              <Numerator>1.333027e-06</Numerator>
              <Numerator>5.295136e-07</Numerator>
              <Numerator>-6.566606e-07</Numerator>
              <Numerator>-5.050541e-07</Numerator>
              <Numerator>2.380756e-07</Numerator>
              <Numerator>3.576771e-07</Numerator>
              <Numerator>-2.93251e-08</Numerator>
              <Numerator>-2.029251e-07</Numerator>
              <Numerator>-4.377202e-08</Numerator>
              <Numerator>9.04852e-08</Numerator>
              <Numerator>4.823501e-08</Numerator>
              <Numerator>-2.774098e-08</Numerator>
              <Numerator>-2.973504e-08</Numerator>
              <Numerator>2.18423e-09</Numerator>
              <Numerator>1.240319e-08</Numerator>
              <Numerator>4.73744e-09</Numerator>
              <Numerator>-2.487704e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">200.0</InputSampleRate>
              <Factor>2</Factor>
              <Offset>0</Offset>
              <Delay>0.555</Delay>
              <Correction>0.555</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
        </Response>
      </Channel>
      <Channel code="HHN" startDate="2016-02-24T00:00:00.000000Z" endDate="2025-12-31T00:00:00.000000Z" locationCode="">
        <Latitude unit="DEGREES">0.0</Latitude>
        <Longitude unit="DEGREES">0.0</Longitude>
        <Elevation unit="METERS">0.0</Elevation>
        <Depth unit="METERS">0.0</Depth>
        <SampleRate>100.0</SampleRate>
        <Response>
          <InstrumentSensitivity>
            <Value>301720003.7617996</Value>
            <Frequency>1.0</Frequency>
            <InputUnits>
              <Name>M/S</Name>
              <Description>Velocity in Meters per Second</Description>
            </InputUnits>
            <OutputUnits>
              <Name>COUNTS</Name>
              <Description>Digital Counts</Description>
            </OutputUnits>
          </InstrumentSensitivity>
          <Stage number="1">
            <PolesZeros>
              <InputUnits>
                <Name>M/S</Name>
                <Description>Velocity in Meters per Second</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>4.344928e+17</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
              <Zero number="0">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="1">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="2">
                <Real minusError="-392.0" plusError="-392.0">-392.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="3">
                <Real minusError="-1960.0" plusError="-1960.0">-1960.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="4">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="1740.0" plusError="1740.0">1740.0</Imaginary>
              </Zero>
              <Zero number="5">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="-1740.0" plusError="-1740.0">-1740.0</Imaginary>
              </Zero>
              <Pole number="0">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="0.03702" plusError="0.03702">0.03702</Imaginary>
              </Pole>
              <Pole number="1">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="-0.03702" plusError="-0.03702">-0.03702</Imaginary>
              </Pole>
              <Pole number="2">
                <Real minusError="-343.0" plusError="-343.0">-343.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="3">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="467.0" plusError="467.0">467.0</Imaginary>
              </Pole>
              <Pole number="4">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="-467.0" plusError="-467.0">-467.0</Imaginary>
              </Pole>
              <Pole number="5">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="1522.0" plusError="1522.0">1522.0</Imaginary>
              </Pole>
              <Pole number="6">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="-1522.0" plusError="-1522.0">-1522.0</Imaginary>
              </Pole>
              <Pole number="7">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="4700.0" plusError="4700.0">4700.0</Imaginary>
              </Pole>
              <Pole number="8">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="-4700.0" plusError="-4700.0">-4700.0</Imaginary>
              </Pole>
              <Pole number="9">
                <Real minusError="-6900.0" plusError="-6900.0">-6900.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="10">
                <Real minusError="-15000.0" plusError="-15000.0">-15000.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
            </PolesZeros>
            <StageGain>
              <Value>754.3</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="2">
            <PolesZeros>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>1.0</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
            </PolesZeros>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="3">
            <Coefficients>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>1.0</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>1</Factor>
              <Offset>0</Offset>
              <Delay>0.0</Delay>
              <Correction>0.0</Correction>
            </Decimation>
            <StageGain>
              <Value>400000.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="4">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-4.047908e-10</Numerator>
              <Numerator>-1.390291e-10</Numerator>
              <Numerator>6.728001e-10</Numerator>
              <Numerator>2.757972e-09</Numerator>
              <Numerator>7.546507e-09</Numerator>
              <Numerator>1.766681e-08</Numerator>
              <Numerator>3.769363e-08</Numerator>
              <Numerator>7.523132e-08</Numerator>
              <Numerator>1.424254e-07</Numerator>
              <Numerator>2.57999e-07</Numerator>
              <Numerator>4.499037e-07</Numerator>
              <Numerator>7.586555e-07</Numerator>
              <Numerator>1.241386e-06</Numerator>
              <Numerator>1.97658e-06</Numerator>
              <Numerator>3.069389e-06</Numerator>
              <Numerator>4.657284e-06</Numerator>
              <Numerator>6.915693e-06</Numerator>
              <Numerator>1.00631e-05</Numerator>
              <Numerator>1.436487e-05</Numerator>
              <Numerator>2.013499e-05</Numerator>
              <Numerator>2.773459e-05</Numerator>
              <Numerator>3.756609e-05</Numerator>
              <Numerator>5.006174e-05</Numerator>
              <Numerator>6.566517e-05</Numerator>
              <Numerator>8.480489e-05</Numerator>
              <Numerator>0.0001078587</Numerator>
              <Numerator>0.0001351084</Numerator>
              <Numerator>0.0001666851</Numerator>
              <Numerator>0.0002025053</Numerator>
              <Numerator>0.0002421999</Numerator>
              <Numerator>0.000285038</Numerator>
              <Numerator>0.0003298504</Numerator>
              <Numerator>0.000374956</Numerator>
              <Numerator>0.0004180986</Numerator>
              <Numerator>0.0004564003</Numerator>
              <Numerator>0.0004863386</Numerator>
              <Numerator>0.0005037566</Numerator>
              <Numerator>0.0005039131</Numerator>
              <Numerator>0.0004815801</Numerator>
              <Numerator>0.0004311946</Numerator>
              <Numerator>0.000347068</Numerator>
              <Numerator>0.0002236552</Numerator>
              <Numerator>5.588177e-05</Numerator>
              <Numerator>-0.0001604755</Numerator>
              <Numerator>-0.0004283654</Numerator>
              <Numerator>-0.0007490084</Numerator>
              <Numerator>-0.001121432</Numerator>
              <Numerator>-0.001542013</Numerator>
              <Numerator>-0.002004062</Numerator>
              <Numerator>-0.002497462</Numerator>
              <Numerator>-0.003008406</Numerator>
              <Numerator>-0.00351925</Numerator>
              <Numerator>-0.004008517</Numerator>
              <Numerator>-0.00445107</Numerator>
              <Numerator>-0.004818468</Numerator>
              <Numerator>-0.005079526</Numerator>
              <Numerator>-0.005201073</Numerator>
              <Numerator>-0.005148892</Numerator>
              <Numerator>-0.004888844</Numerator>
              <Numerator>-0.004388128</Numerator>
              <Numerator>-0.003616642</Numerator>
              <Numerator>-0.002548397</Numerator>
              <Numerator>-0.00116293</Numerator>
              <Numerator>0.0005533497</Numerator>
              <Numerator>0.002605953</Numerator>
              <Numerator>0.004991292</Numerator>
              <Numerator>0.007695918</Numerator>
              <Numerator>0.01069608</Numerator>
              <Numerator>0.01395761</Numerator>
              <Numerator>0.01743625</Numerator>
              <Numerator>0.02107831</Numerator>
              <Numerator>0.02482173</Numerator>
              <Numerator>0.02859758</Numerator>
              <Numerator>0.03233183</Numerator>
              <Numerator>0.0359474</Numerator>
              <Numerator>0.03936644</Numerator>
              <Numerator>0.04251273</Numerator>
              <Numerator>0.04531409</Numerator>
              <Numerator>0.04770474</Numerator>
              <Numerator>0.04962748</Numerator>
              <Numerator>0.05103565</Numerator>
              <Numerator>0.05189471</Numerator>
              <Numerator>0.05218345</Numerator>
              <Numerator>0.05189471</Numerator>
              <Numerator>0.05103565</Numerator>
              <Numerator>0.04962748</Numerator>
              <Numerator>0.04770474</Numerator>
              <Numerator>0.04531409</Numerator>
              <Numerator>0.04251273</Numerator>
              <Numerator>0.03936644</Numerator>
              <Numerator>0.0359474</Numerator>
              <Numerator>0.03233183</Numerator>
              <Numerator>0.02859758</Numerator>
              <Numerator>0.02482173</Numerator>
              <Numerator>0.02107831</Numerator>
              <Numerator>0.01743625</Numerator>
              <Numerator>0.01395761</Numerator>
              <Numerator>0.01069608</Numerator>
              <Numerator>0.007695918</Numerator>
              <Numerator>0.004991292</Numerator>
              <Numerator>0.002605953</Numerator>
              <Numerator>0.0005533497</Numerator>
              <Numerator>-0.00116293</Numerator>
              <Numerator>-0.002548397</Numerator>
              <Numerator>-0.003616642</Numerator>
              <Numerator>-0.004388128</Numerator>
              <Numerator>-0.004888844</Numerator>
              <Numerator>-0.005148892</Numerator>
              <Numerator>-0.005201073</Numerator>
              <Numerator>-0.005079526</Numerator>
              <Numerator>-0.004818468</Numerator>
              <Numerator>-0.00445107</Numerator>
              <Numerator>-0.004008517</Numerator>
              <Numerator>-0.00351925</Numerator>
              <Numerator>-0.003008406</Numerator>
              <Numerator>-0.002497462</Numerator>
              <Numerator>-0.002004062</Numerator>
              <Numerator>-0.001542013</Numerator>
              <Numerator>-0.001121432</Numerator>
              <Numerator>-0.0007490084</Numerator>
              <Numerator>-0.0004283654</Numerator>
              <Numerator>-0.0001604755</Numerator>
              <Numerator>5.588177e-05</Numerator>
              <Numerator>0.0002236552</Numerator>
              <Numerator>0.000347068</Numerator>
              <Numerator>0.0004311946</Numerator>
              <Numerator>0.0004815801</Numerator>
              <Numerator>0.0005039131</Numerator>
              <Numerator>0.0005037566</Numerator>
              <Numerator>0.0004863386</Numerator>
              <Numerator>0.0004564003</Numerator>
              <Numerator>0.0004180986</Numerator>
              <Numerator>0.000374956</Numerator>
              <Numerator>0.0003298504</Numerator>
              <Numerator>0.000285038</Numerator>
              <Numerator>0.0002421999</Numerator>
              <Numerator>0.0002025053</Numerator>
              <Numerator>0.0001666851</Numerator>
              <Numerator>0.0001351084</Numerator>
              <Numerator>0.0001078587</Numerator>
              <Numerator>8.480489e-05</Numerator>
              <Numerator>6.566517e-05</Numerator>
              <Numerator>5.006174e-05</Numerator>
              <Numerator>3.756609e-05</Numerator>
              <Numerator>2.773459e-05</Numerator>
              <Numerator>2.013499e-05</Numerator>
              <Numerator>1.436487e-05</Numerator>
              <Numerator>1.00631e-05</Numerator>
              <Numerator>6.915693e-06</Numerator>
              <Numerator>4.657284e-06</Numerator>
              <Numerator>3.069389e-06</Numerator>
              <Numerator>1.97658e-06</Numerator>
              <Numerator>1.241386e-06</Numerator>
              <Numerator>7.586555e-07</Numerator>
              <Numerator>4.499037e-07</Numerator>
              <Numerator>2.57999e-07</Numerator>
              <Numerator>1.424254e-07</Numerator>
              <Numerator>7.523132e-08</Numerator>
              <Numerator>3.769363e-08</Numerator>
              <Numerator>1.766681e-08</Numerator>
              <Numerator>7.546507e-09</Numerator>
              <Numerator>2.757972e-09</Numerator>
              <Numerator>6.728001e-10</Numerator>
              <Numerator>-1.390291e-10</Numerator>
              <Numerator>-4.047908e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>15</Factor>
              <Offset>0</Offset>
              <Delay>0.002733333</Delay>
              <Correction>0.002733333</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="5">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>8.46923e-10</Numerator>
              <Numerator>2.27422e-09</Numerator>
              <Numerator>4.538951e-09</Numerator>
              <Numerator>6.873791e-09</Numerator>
              <Numerator>7.10904e-09</Numerator>
              <Numerator>7.627841e-10</Numerator>
              <Numerator>-1.98301e-08</Numerator>
              <Numerator>-6.609942e-08</Numerator>
              <Numerator>-1.531138e-07</Numerator>
              <Numerator>-2.982495e-07</Numerator>
              <Numerator>-5.181519e-07</Numerator>
              <Numerator>-8.236356e-07</Numerator>
              <Numerator>-1.212476e-06</Numerator>
              <Numerator>-1.660555e-06</Numerator>
              <Numerator>-2.112474e-06</Numerator>
              <Numerator>-2.473531e-06</Numerator>
              <Numerator>-2.605619e-06</Numerator>
              <Numerator>-2.330134e-06</Numerator>
              <Numerator>-1.44098e-06</Numerator>
              <Numerator>2.698043e-07</Numerator>
              <Numerator>2.972714e-06</Numerator>
              <Numerator>6.748858e-06</Numerator>
              <Numerator>1.152962e-05</Numerator>
              <Numerator>1.703543e-05</Numerator>
              <Numerator>2.272479e-05</Numerator>
              <Numerator>2.776698e-05</Numerator>
              <Numerator>3.105368e-05</Numerator>
              <Numerator>3.126302e-05</Numerator>
              <Numerator>2.698613e-05</Numerator>
              <Numerator>1.691886e-05</Numerator>
              <Numerator>1.111765e-07</Numerator>
              <Numerator>-2.374559e-05</Numerator>
              <Numerator>-5.402672e-05</Numerator>
              <Numerator>-8.892268e-05</Numerator>
              <Numerator>-0.0001252819</Numerator>
              <Numerator>-0.0001586044</Numerator>
              <Numerator>-0.0001832359</Numerator>
              <Numerator>-0.000192798</Numerator>
              <Numerator>-0.0001808636</Numerator>
              <Numerator>-0.0001418502</Numerator>
              <Numerator>-7.206699e-05</Numerator>
              <Numerator>2.919376e-05</Numerator>
              <Numerator>0.0001586655</Numerator>
              <Numerator>0.0003083858</Numerator>
              <Numerator>0.0004654217</Numerator>
              <Numerator>0.0006121983</Numerator>
              <Numerator>0.0007275471</Numerator>
              <Numerator>0.0007885116</Numerator>
              <Numerator>0.0007728578</Numerator>
              <Numerator>0.000662123</Numerator>
              <Numerator>0.000444926</Numerator>
              <Numerator>0.0001201614</Numerator>
              <Numerator>-0.0003003695</Numerator>
              <Numerator>-0.0007903605</Numerator>
              <Numerator>-0.001308874</Numerator>
              <Numerator>-0.00180202</Numerator>
              <Numerator>-0.002206618</Numerator>
              <Numerator>-0.00245579</Numerator>
              <Numerator>-0.002486192</Numerator>
              <Numerator>-0.002246312</Numerator>
              <Numerator>-0.001705031</Numerator>
              <Numerator>-0.0008594633</Numerator>
              <Numerator>0.0002590112</Numerator>
              <Numerator>0.001581566</Numerator>
              <Numerator>0.003002498</Numerator>
              <Numerator>0.004384142</Numerator>
              <Numerator>0.005566316</Numerator>
              <Numerator>0.006380002</Numerator>
              <Numerator>0.006664402</Numerator>
              <Numerator>0.006286043</Numerator>
              <Numerator>0.005158141</Numerator>
              <Numerator>0.003258199</Numerator>
              <Numerator>0.0006416821</Numerator>
              <Numerator>-0.002550179</Numerator>
              <Numerator>-0.006090065</Numerator>
              <Numerator>-0.009672703</Numerator>
              <Numerator>-0.01293168</Numerator>
              <Numerator>-0.01546425</Numerator>
              <Numerator>-0.01686256</Numerator>
              <Numerator>-0.01674898</Numerator>
              <Numerator>-0.01481246</Numerator>
              <Numerator>-0.01084255</Numerator>
              <Numerator>-0.004757783</Numerator>
              <Numerator>0.003374886</Numerator>
              <Numerator>0.01333183</Numerator>
              <Numerator>0.02473738</Numerator>
              <Numerator>0.03708165</Numerator>
              <Numerator>0.0497507</Numerator>
              <Numerator>0.06206696</Numerator>
              <Numerator>0.07333685</Numerator>
              <Numerator>0.08290152</Numerator>
              <Numerator>0.0901866</Numerator>
              <Numerator>0.09474635</Numerator>
              <Numerator>0.09629848</Numerator>
              <Numerator>0.09474635</Numerator>
              <Numerator>0.0901866</Numerator>
              <Numerator>0.08290152</Numerator>
              <Numerator>0.07333685</Numerator>
              <Numerator>0.06206696</Numerator>
              <Numerator>0.0497507</Numerator>
              <Numerator>0.03708165</Numerator>
              <Numerator>0.02473738</Numerator>
              <Numerator>0.01333183</Numerator>
              <Numerator>0.003374886</Numerator>
              <Numerator>-0.004757783</Numerator>
              <Numerator>-0.01084255</Numerator>
              <Numerator>-0.01481246</Numerator>
              <Numerator>-0.01674898</Numerator>
              <Numerator>-0.01686256</Numerator>
              <Numerator>-0.01546425</Numerator>
              <Numerator>-0.01293168</Numerator>
              <Numerator>-0.009672703</Numerator>
              <Numerator>-0.006090065</Numerator>
              <Numerator>-0.002550179</Numerator>
              <Numerator>0.0006416821</Numerator>
              <Numerator>0.003258199</Numerator>
              <Numerator>0.005158141</Numerator>
              <Numerator>0.006286043</Numerator>
              <Numerator>0.006664402</Numerator>
              <Numerator>0.006380002</Numerator>
              <Numerator>0.005566316</Numerator>
              <Numerator>0.004384142</Numerator>
              <Numerator>0.003002498</Numerator>
              <Numerator>0.001581566</Numerator>
              <Numerator>0.0002590112</Numerator>
              <Numerator>-0.0008594633</Numerator>
              <Numerator>-0.001705031</Numerator>
              <Numerator>-0.002246312</Numerator>
              <Numerator>-0.002486192</Numerator>
              <Numerator>-0.00245579</Numerator>
              <Numerator>-0.002206618</Numerator>
              <Numerator>-0.00180202</Numerator>
              <Numerator>-0.001308874</Numerator>
              <Numerator>-0.0007903605</Numerator>
              <Numerator>-0.0003003695</Numerator>
              <Numerator>0.0001201614</Numerator>
              <Numerator>0.000444926</Numerator>
              <Numerator>0.000662123</Numerator>
              <Numerator>0.0007728578</Numerator>
              <Numerator>0.0007885116</Numerator>
              <Numerator>0.0007275471</Numerator>
              <Numerator>0.0006121983</Numerator>
              <Numerator>0.0004654217</Numerator>
              <Numerator>0.0003083858</Numerator>
              <Numerator>0.0001586655</Numerator>
              <Numerator>2.919376e-05</Numerator>
              <Numerator>-7.206699e-05</Numerator>
              <Numerator>-0.0001418502</Numerator>
              <Numerator>-0.0001808636</Numerator>
              <Numerator>-0.000192798</Numerator>
              <Numerator>-0.0001832359</Numerator>
              <Numerator>-0.0001586044</Numerator>
              <Numerator>-0.0001252819</Numerator>
              <Numerator>-8.892268e-05</Numerator>
              <Numerator>-5.402672e-05</Numerator>
              <Numerator>-2.374559e-05</Numerator>
              <Numerator>1.111765e-07</Numerator>
              <Numerator>1.691886e-05</Numerator>
              <Numerator>2.698613e-05</Numerator>
              <Numerator>3.126302e-05</Numerator>
              <Numerator>3.105368e-05</Numerator>
              <Numerator>2.776698e-05</Numerator>
              <Numerator>2.272479e-05</Numerator>
              <Numerator>1.703543e-05</Numerator>
              <Numerator>1.152962e-05</Numerator>
              <Numerator>6.748858e-06</Numerator>
              <Numerator>2.972714e-06</Numerator>
              <Numerator>2.698043e-07</Numerator>
              <Numerator>-1.44098e-06</Numerator>
              <Numerator>-2.330134e-06</Numerator>
              <Numerator>-2.605619e-06</Numerator>
              <Numerator>-2.473531e-06</Numerator>
              <Numerator>-2.112474e-06</Numerator>
              <Numerator>-1.660555e-06</Numerator>
              <Numerator>-1.212476e-06</Numerator>
              <Numerator>-8.236356e-07</Numerator>
              <Numerator>-5.181519e-07</Numerator>
              <Numerator>-2.982495e-07</Numerator>
              <Numerator>-1.531138e-07</Numerator>
              <Numerator>-6.609942e-08</Numerator>
              <Numerator>-1.98301e-08</Numerator>
              <Numerator>7.627841e-10</Numerator>
              <Numerator>7.10904e-09</Numerator>
              <Numerator>6.873791e-09</Numerator>
              <Numerator>4.538951e-09</Numerator>
              <Numerator>2.27422e-09</Numerator>
              <Numerator>8.46923e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">2000.0</InputSampleRate>
              <Factor>10</Factor>
              <Offset>0</Offset>
              <Delay>0.0465</Delay>
              <Correction>0.0465</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="6">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-2.487704e-10</Numerator>
              <Numerator>4.73744e-09</Numerator>
              <Numerator>1.240319e-08</Numerator>
              <Numerator>2.18423e-09</Numerator>
              <Numerator>-2.973504e-08</Numerator>
              <Numerator>-2.774098e-08</Numerator>
              <Numerator>4.823501e-08</Numerator>
              <Numerator>9.04852e-08</Numerator>
              <Numerator>-4.377202e-08</Numerator>
              <Numerator>-2.029251e-07</Numerator>
              <Numerator>-2.93251e-08</Numerator>
              <Numerator>3.576771e-07</Numerator>
              <Numerator>2.380756e-07</Numerator>
              <Numerator>-5.050541e-07</Numerator>
              <Numerator>-6.566606e-07</Numerator>
              <Numerator>5.295136e-07</Numerator>
              <Numerator>1.333027e-06</Numerator>
              <Numerator>-2.353909e-07</Numerator>
              <Numerator>-2.234558e-06</Numerator>
              <Numerator>-6.431887e-07</Numerator>
              <Numerator>3.178848e-06</Numerator>
              <Numerator>2.391894e-06</Numerator>
              <Numerator>-3.766426e-06</Numerator>
              <Numerator>-5.213131e-06</Numerator>
              <Numerator>3.343879e-06</Numerator>
              <Numerator>9.069842e-06</Numerator>
              <Numerator>-1.034203e-06</Numerator>
              <Numerator>-1.349476e-05</Numerator>
              <Numerator>-4.128203e-06</Numerator>
              <Numerator>1.740814e-05</Numerator>
              <Numerator>1.293247e-05</Numerator>
              <Numerator>-1.901116e-05</Numerator>
              <Numerator>-2.55982e-05</Numerator>
              <Numerator>1.583847e-05</Numerator>
              <Numerator>4.129854e-05</Numerator>
              <Numerator>-5.051362e-06</Numerator>
              <Numerator>-5.769434e-05</Numerator>
              <Numerator>-1.597343e-05</Numerator>
              <Numerator>7.06232e-05</Numerator>
              <Numerator>4.876212e-05</Numerator>
              <Numerator>-7.411825e-05</Numerator>
              <Numerator>-9.265601e-05</Numerator>
              <Numerator>6.092806e-05</Numerator>
              <Numerator>0.0001437042</Numerator>
              <Numerator>-2.365713e-05</Numerator>
              <Numerator>-0.0001938177</Numerator>
              <Numerator>-4.346068e-05</Numerator>
              <Numerator>0.0002305286</Numerator>
              <Numerator>0.0001422997</Numerator>
              <Numerator>-0.0002376966</Numerator>
              <Numerator>-0.0002684195</Numerator>
              <Numerator>0.00019742</Numerator>
              <Numerator>0.0004089862</Numerator>
              <Numerator>-9.322642e-05</Numerator>
              <Numerator>-0.0005416667</Numerator>
              <Numerator>-8.56506e-05</Numerator>
              <Numerator>0.0006351459</Numerator>
              <Numerator>0.0003394235</Numerator>
              <Numerator>-0.0006517938</Numerator>
              <Numerator>-0.0006531623</Numerator>
              <Numerator>0.000552734</Numerator>
              <Numerator>0.0009935334</Numerator>
              <Numerator>-0.000305133</Numerator>
              <Numerator>-0.00130802</Numerator>
              <Numerator>-0.0001089867</Numerator>
              <Numerator>0.001527642</Numerator>
              <Numerator>0.0006836461</Numerator>
              <Numerator>-0.001573808</Numerator>
              <Numerator>-0.00138119</Numerator>
              <Numerator>0.001369316</Numerator>
              <Numerator>0.002127841</Numerator>
              <Numerator>-0.0008527391</Numerator>
              <Numerator>-0.002814326</Numerator>
              <Numerator>-5.435981e-06</Numerator>
              <Numerator>0.003302926</Numerator>
              <Numerator>0.001187235</Numerator>
              <Numerator>-0.003441493</Numerator>
              <Numerator>-0.002615018</Numerator>
              <Numerator>0.003083861</Numerator>
              <Numerator>0.004145541</Numerator>
              <Numerator>-0.002114933</Numerator>
              <Numerator>-0.005572669</Numerator>
              <Numerator>0.0004775432</Numerator>
              <Numerator>0.006640171</Numerator>
              <Numerator>0.001802538</Numerator>
              <Numerator>-0.00706464</Numerator>
              <Numerator>-0.004597381</Numerator>
              <Numerator>0.00656694</Numerator>
              <Numerator>0.007666904</Numerator>
              <Numerator>-0.00490895</Numerator>
              <Numerator>-0.01066029</Numerator>
              <Numerator>0.001931064</Numerator>
              <Numerator>0.01312888</Numerator>
              <Numerator>0.002414871</Numerator>
              <Numerator>-0.01454758</Numerator>
              <Numerator>-0.008042475</Numerator>
              <Numerator>0.01433728</Numerator>
              <Numerator>0.01472206</Numerator>
              <Numerator>-0.01187359</Numerator>
              <Numerator>-0.02208895</Numerator>
              <Numerator>0.00645106</Numerator>
              <Numerator>0.0296694</Numerator>
              <Numerator>0.002871719</Numerator>
              <Numerator>-0.03692219</Numerator>
              <Numerator>-0.01777635</Numerator>
              <Numerator>0.04329151</Numerator>
              <Numerator>0.04248361</Numerator>
              <Numerator>-0.04826485</Numerator>
              <Numerator>-0.09280869</Numerator>
              <Numerator>0.05142858</Numerator>
              <Numerator>0.3137774</Numerator>
              <Numerator>0.4474858</Numerator>
              <Numerator>0.3137774</Numerator>
              <Numerator>0.05142858</Numerator>
              <Numerator>-0.09280869</Numerator>
              <Numerator>-0.04826485</Numerator>
              <Numerator>0.04248361</Numerator>
              <Numerator>0.04329151</Numerator>
              <Numerator>-0.01777635</Numerator>
              <Numerator>-0.03692219</Numerator>
              <Numerator>0.002871719</Numerator>
              <Numerator>0.0296694</Numerator>
              <Numerator>0.00645106</Numerator>
              <Numerator>-0.02208895</Numerator>
              <Numerator>-0.01187359</Numerator>
              <Numerator>0.01472206</Numerator>
              <Numerator>0.01433728</Numerator>
              <Numerator>-0.008042475</Numerator>
              <Numerator>-0.01454758</Numerator>
              <Numerator>0.002414871</Numerator>
              <Numerator>0.01312888</Numerator>
              <Numerator>0.001931064</Numerator>
              <Numerator>-0.01066029</Numerator>
              <Numerator>-0.00490895</Numerator>
              <Numerator>0.007666904</Numerator>
              <Numerator>0.00656694</Numerator>
              <Numerator>-0.004597381</Numerator>
              <Numerator>-0.00706464</Numerator>
              <Numerator>0.001802538</Numerator>
              <Numerator>0.006640171</Numerator>
              <Numerator>0.0004775432</Numerator>
              <Numerator>-0.005572669</Numerator>
              <Numerator>-0.002114933</Numerator>
              <Numerator>0.004145541</Numerator>
              <Numerator>0.003083861</Numerator>
              <Numerator>-0.002615018</Numerator>
              <Numerator>-0.003441493</Numerator>
              <Numerator>0.001187235</Numerator>
              <Numerator>0.003302926</Numerator>
              <Numerator>-5.435981e-06</Numerator>
              <Numerator>-0.002814326</Numerator>
              <Numerator>-0.0008527391</Numerator>
              <Numerator>0.002127841</Numerator>
              <Numerator>0.001369316</Numerator>
              <Numerator>-0.00138119</Numerator>
              <Numerator>-0.001573808</Numerator>
              <Numerator>0.0006836461</Numerator>
              <Numerator>0.001527642</Numerator>
              <Numerator>-0.0001089867</Numerator>
              <Numerator>-0.00130802</Numerator>
              <Numerator>-0.000305133</Numerator>
              <Numerator>0.0009935334</Numerator>
              <Numerator>0.000552734</Numerator>
              <Numerator>-0.0006531623</Numerator>
              <Numerator>-0.0006517938</Numerator>
              <Numerator>0.0003394235</Numerator>
              <Numerator>0.0006351459</Numerator>
              <Numerator>-8.56506e-05</Numerator>
              <Numerator>-0.0005416667</Numerator>
              <Numerator>-9.322642e-05</Numerator>
              <Numerator>0.0004089862</Numerator>
              <Numerator>0.00019742</Numerator>
              <Numerator>-0.0002684195</Numerator>
              <Numerator>-0.0002376966</Numerator>
              <Numerator>0.0001422997</Numerator>
              <Numerator>0.0002305286</Numerator>
              <Numerator>-4.346068e-05</Numerator>
              <Numerator>-0.0001938177</Numerator>
              <Numerator>-2.365713e-05</Numerator>
              <Numerator>0.0001437042</Numerator>
              <Numerator>6.092806e-05</Numerator>
              <Numerator>-9.265601e-05</Numerator>
              <Numerator>-7.411825e-05</Numerator>
              <Numerator>4.876212e-05</Numerator>
              <Numerator>7.06232e-05</Numerator>
              <Numerator>-1.597343e-05</Numerator>
              <Numerator>-5.769434e-05</Numerator>
              <Numerator>-5.051362e-06</Numerator>
              <Numerator>4.129854e-05</Numerator>
              <Numerator>1.583847e-05</Numerator>
              <Numerator>-2.55982e-05</Numerator>
              <Numerator>-1.901116e-05</Numerator>
              <Numerator>1.293247e-05</Numerator>
              <Numerator>1.740814e-05</Numerator>
              <Numerator>-4.128203e-06</Numerator>
              <Numerator>-1.349476e-05</Numerator>
              <Numerator>-1.034203e-06</Numerator>
              <Numerator>9.069842e-06</Numerator>
              <Numerator>3.343879e-06</Numerator>
              <Numerator>-5.213131e-06</Numerator>
              <Numerator>-3.766426e-06</Numerator>
              <Numerator>2.391894e-06</Numerator>
              <Numerator>3.178848e-06</Numerator>
              <Numerator>-6.431887e-07</Numerator>
              <Numerator>-2.234558e-06</Numerator>
              <Numerator>-2.353909e-07</Numerator>
              <Numerator>1.333027e-06</Numerator>
              <Numerator>5.295136e-07</Numerator>
              <Numerator>-6.566606e-07</Numerator>
              <Numerator>-5.050541e-07</Numerator>
              <Numerator>2.380756e-07</Numerator>
              <Numerator>3.576771e-07</Numerator>
              <Numerator>-2.93251e-08</Numerator>
              <Numerator>-2.029251e-07</Numerator>
              <Numerator>-4.377202e-08</Numerator>
              <Numerator>9.04852e-08</Numerator>
              <Numerator>4.823501e-08</Numerator>
              <Numerator>-2.774098e-08</Numerator>
              <Numerator>-2.973504e-08</Numerator>
              <Numerator>2.18423e-09</Numerator>
              <Numerator>1.240319e-08</Numerator>
              <Numerator>4.73744e-09</Numerator>
              <Numerator>-2.487704e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">200.0</InputSampleRate>
              <Factor>2</Factor>
              <Offset>0</Offset>
              <Delay>0.555</Delay>
              <Correction>0.555</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
        </Response>
      </Channel>
      <Channel code="HHE" startDate="2016-02-24T00:00:00.000000Z" endDate="2025-12-31T00:00:00.000000Z" locationCode="">
        <Latitude unit="DEGREES">0.0</Latitude>
        <Longitude unit="DEGREES">0.0</Longitude>
        <Elevation unit="METERS">0.0</Elevation>
        <Depth unit="METERS">0.0</Depth>
        <SampleRate>100.0</SampleRate>
        <Response>
          <InstrumentSensitivity>
            <Value>301720003.7617996</Value>
            <Frequency>1.0</Frequency>
            <InputUnits>
              <Name>M/S</Name>
              <Description>Velocity in Meters per Second</Description>
            </InputUnits>
            <OutputUnits>
              <Name>COUNTS</Name>
              <Description>Digital Counts</Description>
            </OutputUnits>
          </InstrumentSensitivity>
          <Stage number="1">
            <PolesZeros>
              <InputUnits>
                <Name>M/S</Name>
                <Description>Velocity in Meters per Second</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>4.344928e+17</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
              <Zero number="0">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="1">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="2">
                <Real minusError="-392.0" plusError="-392.0">-392.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="3">
                <Real minusError="-1960.0" plusError="-1960.0">-1960.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="4">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="1740.0" plusError="1740.0">1740.0</Imaginary>
              </Zero>
              <Zero number="5">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="-1740.0" plusError="-1740.0">-1740.0</Imaginary>
              </Zero>
              <Pole number="0">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="0.03702" plusError="0.03702">0.03702</Imaginary>
              </Pole>
              <Pole number="1">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="-0.03702" plusError="-0.03702">-0.03702</Imaginary>
              </Pole>
              <Pole number="2">
                <Real minusError="-343.0" plusError="-343.0">-343.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="3">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="467.0" plusError="467.0">467.0</Imaginary>
              </Pole>
              <Pole number="4">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="-467.0" plusError="-467.0">-467.0</Imaginary>
              </Pole>
              <Pole number="5">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="1522.0" plusError="1522.0">1522.0</Imaginary>
              </Pole>
              <Pole number="6">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="-1522.0" plusError="-1522.0">-1522.0</Imaginary>
              </Pole>
              <Pole number="7">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="4700.0" plusError="4700.0">4700.0</Imaginary>
              </Pole>
              <Pole number="8">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="-4700.0" plusError="-4700.0">-4700.0</Imaginary>
              </Pole>
              <Pole number="9">
                <Real minusError="-6900.0" plusError="-6900.0">-6900.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="10">
                <Real minusError="-15000.0" plusError="-15000.0">-15000.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
            </PolesZeros>
            <StageGain>
              <Value>754.3</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="2">
            <PolesZeros>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>1.0</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
            </PolesZeros>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="3">
            <Coefficients>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>1.0</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>1</Factor>
              <Offset>0</Offset>
              <Delay>0.0</Delay>
              <Correction>0.0</Correction>
            </Decimation>
            <StageGain>
              <Value>400000.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="4">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-4.047908e-10</Numerator>
              <Numerator>-1.390291e-10</Numerator>
              <Numerator>6.728001e-10</Numerator>
              <Numerator>2.757972e-09</Numerator>
              <Numerator>7.546507e-09</Numerator>
              <Numerator>1.766681e-08</Numerator>
              <Numerator>3.769363e-08</Numerator>
              <Numerator>7.523132e-08</Numerator>
              <Numerator>1.424254e-07</Numerator>
              <Numerator>2.57999e-07</Numerator>
              <Numerator>4.499037e-07</Numerator>
              <Numerator>7.586555e-07</Numerator>
              <Numerator>1.241386e-06</Numerator>
              <Numerator>1.97658e-06</Numerator>
              <Numerator>3.069389e-06</Numerator>
              <Numerator>4.657284e-06</Numerator>
              <Numerator>6.915693e-06</Numerator>
              <Numerator>1.00631e-05</Numerator>
              <Numerator>1.436487e-05</Numerator>
              <Numerator>2.013499e-05</Numerator>
              <Numerator>2.773459e-05</Numerator>
              <Numerator>3.756609e-05</Numerator>
              <Numerator>5.006174e-05</Numerator>
              <Numerator>6.566517e-05</Numerator>
              <Numerator>8.480489e-05</Numerator>
              <Numerator>0.0001078587</Numerator>
              <Numerator>0.0001351084</Numerator>
              <Numerator>0.0001666851</Numerator>
              <Numerator>0.0002025053</Numerator>
              <Numerator>0.0002421999</Numerator>
              <Numerator>0.000285038</Numerator>
              <Numerator>0.0003298504</Numerator>
              <Numerator>0.000374956</Numerator>
              <Numerator>0.0004180986</Numerator>
              <Numerator>0.0004564003</Numerator>
              <Numerator>0.0004863386</Numerator>
              <Numerator>0.0005037566</Numerator>
              <Numerator>0.0005039131</Numerator>
              <Numerator>0.0004815801</Numerator>
              <Numerator>0.0004311946</Numerator>
              <Numerator>0.000347068</Numerator>
              <Numerator>0.0002236552</Numerator>
              <Numerator>5.588177e-05</Numerator>
              <Numerator>-0.0001604755</Numerator>
              <Numerator>-0.0004283654</Numerator>
              <Numerator>-0.0007490084</Numerator>
              <Numerator>-0.001121432</Numerator>
              <Numerator>-0.001542013</Numerator>
              <Numerator>-0.002004062</Numerator>
              <Numerator>-0.002497462</Numerator>
              <Numerator>-0.003008406</Numerator>
              <Numerator>-0.00351925</Numerator>
              <Numerator>-0.004008517</Numerator>
              <Numerator>-0.00445107</Numerator>
              <Numerator>-0.004818468</Numerator>
              <Numerator>-0.005079526</Numerator>
              <Numerator>-0.005201073</Numerator>
              <Numerator>-0.005148892</Numerator>
              <Numerator>-0.004888844</Numerator>
              <Numerator>-0.004388128</Numerator>
              <Numerator>-0.003616642</Numerator>
              <Numerator>-0.002548397</Numerator>
              <Numerator>-0.00116293</Numerator>
              <Numerator>0.0005533497</Numerator>
              <Numerator>0.002605953</Numerator>
              <Numerator>0.004991292</Numerator>
              <Numerator>0.007695918</Numerator>
              <Numerator>0.01069608</Numerator>
              <Numerator>0.01395761</Numerator>
              <Numerator>0.01743625</Numerator>
              <Numerator>0.02107831</Numerator>
              <Numerator>0.02482173</Numerator>
              <Numerator>0.02859758</Numerator>
              <Numerator>0.03233183</Numerator>
              <Numerator>0.0359474</Numerator>
              <Numerator>0.03936644</Numerator>
              <Numerator>0.04251273</Numerator>
              <Numerator>0.04531409</Numerator>
              <Numerator>0.04770474</Numerator>
              <Numerator>0.04962748</Numerator>
              <Numerator>0.05103565</Numerator>
              <Numerator>0.05189471</Numerator>
              <Numerator>0.05218345</Numerator>
              <Numerator>0.05189471</Numerator>
              <Numerator>0.05103565</Numerator>
              <Numerator>0.04962748</Numerator>
              <Numerator>0.04770474</Numerator>
              <Numerator>0.04531409</Numerator>
              <Numerator>0.04251273</Numerator>
              <Numerator>0.03936644</Numerator>
              <Numerator>0.0359474</Numerator>
              <Numerator>0.03233183</Numerator>
              <Numerator>0.02859758</Numerator>
              <Numerator>0.02482173</Numerator>
              <Numerator>0.02107831</Numerator>
              <Numerator>0.01743625</Numerator>
              <Numerator>0.01395761</Numerator>
              <Numerator>0.01069608</Numerator>
              <Numerator>0.007695918</Numerator>
              <Numerator>0.004991292</Numerator>
              <Numerator>0.002605953</Numerator>
              <Numerator>0.0005533497</Numerator>
              <Numerator>-0.00116293</Numerator>
              <Numerator>-0.002548397</Numerator>
              <Numerator>-0.003616642</Numerator>
              <Numerator>-0.004388128</Numerator>
              <Numerator>-0.004888844</Numerator>
              <Numerator>-0.005148892</Numerator>
              <Numerator>-0.005201073</Numerator>
              <Numerator>-0.005079526</Numerator>
              <Numerator>-0.004818468</Numerator>
              <Numerator>-0.00445107</Numerator>
              <Numerator>-0.004008517</Numerator>
              <Numerator>-0.00351925</Numerator>
              <Numerator>-0.003008406</Numerator>
              <Numerator>-0.002497462</Numerator>
              <Numerator>-0.002004062</Numerator>
              <Numerator>-0.001542013</Numerator>
              <Numerator>-0.001121432</Numerator>
              <Numerator>-0.0007490084</Numerator>
              <Numerator>-0.0004283654</Numerator>
              <Numerator>-0.0001604755</Numerator>
              <Numerator>5.588177e-05</Numerator>
              <Numerator>0.0002236552</Numerator>
              <Numerator>0.000347068</Numerator>
              <Numerator>0.0004311946</Numerator>
              <Numerator>0.0004815801</Numerator>
              <Numerator>0.0005039131</Numerator>
              <Numerator>0.0005037566</Numerator>
              <Numerator>0.0004863386</Numerator>
              <Numerator>0.0004564003</Numerator>
              <Numerator>0.0004180986</Numerator>
              <Numerator>0.000374956</Numerator>
              <Numerator>0.0003298504</Numerator>
              <Numerator>0.000285038</Numerator>
              <Numerator>0.0002421999</Numerator>
              <Numerator>0.0002025053</Numerator>
              <Numerator>0.0001666851</Numerator>
              <Numerator>0.0001351084</Numerator>
              <Numerator>0.0001078587</Numerator>
              <Numerator>8.480489e-05</Numerator>
              <Numerator>6.566517e-05</Numerator>
              <Numerator>5.006174e-05</Numerator>
              <Numerator>3.756609e-05</Numerator>
              <Numerator>2.773459e-05</Numerator>
              <Numerator>2.013499e-05</Numerator>
              <Numerator>1.436487e-05</Numerator>
              <Numerator>1.00631e-05</Numerator>
              <Numerator>6.915693e-06</Numerator>
              <Numerator>4.657284e-06</Numerator>
              <Numerator>3.069389e-06</Numerator>
              <Numerator>1.97658e-06</Numerator>
              <Numerator>1.241386e-06</Numerator>
              <Numerator>7.586555e-07</Numerator>
              <Numerator>4.499037e-07</Numerator>
              <Numerator>2.57999e-07</Numerator>
              <Numerator>1.424254e-07</Numerator>
              <Numerator>7.523132e-08</Numerator>
              <Numerator>3.769363e-08</Numerator>
              <Numerator>1.766681e-08</Numerator>
              <Numerator>7.546507e-09</Numerator>
              <Numerator>2.757972e-09</Numerator>
              <Numerator>6.728001e-10</Numerator>
              <Numerator>-1.390291e-10</Numerator>
              <Numerator>-4.047908e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>15</Factor>
              <Offset>0</Offset>
              <Delay>0.002733333</Delay>
              <Correction>0.002733333</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="5">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>8.46923e-10</Numerator>
              <Numerator>2.27422e-09</Numerator>
              <Numerator>4.538951e-09</Numerator>
              <Numerator>6.873791e-09</Numerator>
              <Numerator>7.10904e-09</Numerator>
              <Numerator>7.627841e-10</Numerator>
              <Numerator>-1.98301e-08</Numerator>
              <Numerator>-6.609942e-08</Numerator>
              <Numerator>-1.531138e-07</Numerator>
              <Numerator>-2.982495e-07</Numerator>
              <Numerator>-5.181519e-07</Numerator>
              <Numerator>-8.236356e-07</Numerator>
              <Numerator>-1.212476e-06</Numerator>
              <Numerator>-1.660555e-06</Numerator>
              <Numerator>-2.112474e-06</Numerator>
              <Numerator>-2.473531e-06</Numerator>
              <Numerator>-2.605619e-06</Numerator>
              <Numerator>-2.330134e-06</Numerator>
              <Numerator>-1.44098e-06</Numerator>
              <Numerator>2.698043e-07</Numerator>
              <Numerator>2.972714e-06</Numerator>
              <Numerator>6.748858e-06</Numerator>
              <Numerator>1.152962e-05</Numerator>
              <Numerator>1.703543e-05</Numerator>
              <Numerator>2.272479e-05</Numerator>
              <Numerator>2.776698e-05</Numerator>
              <Numerator>3.105368e-05</Numerator>
              <Numerator>3.126302e-05</Numerator>
              <Numerator>2.698613e-05</Numerator>
              <Numerator>1.691886e-05</Numerator>
              <Numerator>1.111765e-07</Numerator>
              <Numerator>-2.374559e-05</Numerator>
              <Numerator>-5.402672e-05</Numerator>
              <Numerator>-8.892268e-05</Numerator>
              <Numerator>-0.0001252819</Numerator>
              <Numerator>-0.0001586044</Numerator>
              <Numerator>-0.0001832359</Numerator>
              <Numerator>-0.000192798</Numerator>
              <Numerator>-0.0001808636</Numerator>
              <Numerator>-0.0001418502</Numerator>
              <Numerator>-7.206699e-05</Numerator>
              <Numerator>2.919376e-05</Numerator>
              <Numerator>0.0001586655</Numerator>
              <Numerator>0.0003083858</Numerator>
              <Numerator>0.0004654217</Numerator>
              <Numerator>0.0006121983</Numerator>
              <Numerator>0.0007275471</Numerator>
              <Numerator>0.0007885116</Numerator>
              <Numerator>0.0007728578</Numerator>
              <Numerator>0.000662123</Numerator>
              <Numerator>0.000444926</Numerator>
              <Numerator>0.0001201614</Numerator>
              <Numerator>-0.0003003695</Numerator>
              <Numerator>-0.0007903605</Numerator>
              <Numerator>-0.001308874</Numerator>
              <Numerator>-0.00180202</Numerator>
              <Numerator>-0.002206618</Numerator>
              <Numerator>-0.00245579</Numerator>
              <Numerator>-0.002486192</Numerator>
              <Numerator>-0.002246312</Numerator>
              <Numerator>-0.001705031</Numerator>
              <Numerator>-0.0008594633</Numerator>
              <Numerator>0.0002590112</Numerator>
              <Numerator>0.001581566</Numerator>
              <Numerator>0.003002498</Numerator>
              <Numerator>0.004384142</Numerator>
              <Numerator>0.005566316</Numerator>
              <Numerator>0.006380002</Numerator>
              <Numerator>0.006664402</Numerator>
              <Numerator>0.006286043</Numerator>
              <Numerator>0.005158141</Numerator>
              <Numerator>0.003258199</Numerator>
              <Numerator>0.0006416821</Numerator>
              <Numerator>-0.002550179</Numerator>
              <Numerator>-0.006090065</Numerator>
              <Numerator>-0.009672703</Numerator>
              <Numerator>-0.01293168</Numerator>
              <Numerator>-0.01546425</Numerator>
              <Numerator>-0.01686256</Numerator>
              <Numerator>-0.01674898</Numerator>
              <Numerator>-0.01481246</Numerator>
              <Numerator>-0.01084255</Numerator>
              <Numerator>-0.004757783</Numerator>
              <Numerator>0.003374886</Numerator>
              <Numerator>0.01333183</Numerator>
              <Numerator>0.02473738</Numerator>
              <Numerator>0.03708165</Numerator>
              <Numerator>0.0497507</Numerator>
              <Numerator>0.06206696</Numerator>
              <Numerator>0.07333685</Numerator>
              <Numerator>0.08290152</Numerator>
              <Numerator>0.0901866</Numerator>
              <Numerator>0.09474635</Numerator>
              <Numerator>0.09629848</Numerator>
              <Numerator>0.09474635</Numerator>
              <Numerator>0.0901866</Numerator>
              <Numerator>0.08290152</Numerator>
              <Numerator>0.07333685</Numerator>
              <Numerator>0.06206696</Numerator>
              <Numerator>0.0497507</Numerator>
              <Numerator>0.03708165</Numerator>
              <Numerator>0.02473738</Numerator>
              <Numerator>0.01333183</Numerator>
              <Numerator>0.003374886</Numerator>
              <Numerator>-0.004757783</Numerator>
              <Numerator>-0.01084255</Numerator>
              <Numerator>-0.01481246</Numerator>
              <Numerator>-0.01674898</Numerator>
              <Numerator>-0.01686256</Numerator>
              <Numerator>-0.01546425</Numerator>
              <Numerator>-0.01293168</Numerator>
              <Numerator>-0.009672703</Numerator>
              <Numerator>-0.006090065</Numerator>
              <Numerator>-0.002550179</Numerator>
              <Numerator>0.0006416821</Numerator>
              <Numerator>0.003258199</Numerator>
              <Numerator>0.005158141</Numerator>
              <Numerator>0.006286043</Numerator>
              <Numerator>0.006664402</Numerator>
              <Numerator>0.006380002</Numerator>
              <Numerator>0.005566316</Numerator>
              <Numerator>0.004384142</Numerator>
              <Numerator>0.003002498</Numerator>
              <Numerator>0.001581566</Numerator>
              <Numerator>0.0002590112</Numerator>
              <Numerator>-0.0008594633</Numerator>
              <Numerator>-0.001705031</Numerator>
              <Numerator>-0.002246312</Numerator>
              <Numerator>-0.002486192</Numerator>
              <Numerator>-0.00245579</Numerator>
              <Numerator>-0.002206618</Numerator>
              <Numerator>-0.00180202</Numerator>
              <Numerator>-0.001308874</Numerator>
              <Numerator>-0.0007903605</Numerator>
              <Numerator>-0.0003003695</Numerator>
              <Numerator>0.0001201614</Numerator>
              <Numerator>0.000444926</Numerator>
              <Numerator>0.000662123</Numerator>
              <Numerator>0.0007728578</Numerator>
              <Numerator>0.0007885116</Numerator>
              <Numerator>0.0007275471</Numerator>
              <Numerator>0.0006121983</Numerator>
              <Numerator>0.0004654217</Numerator>
              <Numerator>0.0003083858</Numerator>
              <Numerator>0.0001586655</Numerator>
              <Numerator>2.919376e-05</Numerator>
              <Numerator>-7.206699e-05</Numerator>
              <Numerator>-0.0001418502</Numerator>
              <Numerator>-0.0001808636</Numerator>
              <Numerator>-0.000192798</Numerator>
              <Numerator>-0.0001832359</Numerator>
              <Numerator>-0.0001586044</Numerator>
              <Numerator>-0.0001252819</Numerator>
              <Numerator>-8.892268e-05</Numerator>
              <Numerator>-5.402672e-05</Numerator>
              <Numerator>-2.374559e-05</Numerator>
              <Numerator>1.111765e-07</Numerator>
              <Numerator>1.691886e-05</Numerator>
              <Numerator>2.698613e-05</Numerator>
              <Numerator>3.126302e-05</Numerator>
              <Numerator>3.105368e-05</Numerator>
              <Numerator>2.776698e-05</Numerator>
              <Numerator>2.272479e-05</Numerator>
              <Numerator>1.703543e-05</Numerator>
              <Numerator>1.152962e-05</Numerator>
              <Numerator>6.748858e-06</Numerator>
              <Numerator>2.972714e-06</Numerator>
              <Numerator>2.698043e-07</Numerator>
              <Numerator>-1.44098e-06</Numerator>
              <Numerator>-2.330134e-06</Numerator>
              <Numerator>-2.605619e-06</Numerator>
              <Numerator>-2.473531e-06</Numerator>
              <Numerator>-2.112474e-06</Numerator>
              <Numerator>-1.660555e-06</Numerator>
              <Numerator>-1.212476e-06</Numerator>
              <Numerator>-8.236356e-07</Numerator>
              <Numerator>-5.181519e-07</Numerator>
              <Numerator>-2.982495e-07</Numerator>
              <Numerator>-1.531138e-07</Numerator>
              <Numerator>-6.609942e-08</Numerator>
              <Numerator>-1.98301e-08</Numerator>
              <Numerator>7.627841e-10</Numerator>
              <Numerator>7.10904e-09</Numerator>
              <Numerator>6.873791e-09</Numerator>
              <Numerator>4.538951e-09</Numerator>
              <Numerator>2.27422e-09</Numerator>
              <Numerator>8.46923e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">2000.0</InputSampleRate>
              <Factor>10</Factor>
              <Offset>0</Offset>
              <Delay>0.0465</Delay>
              <Correction>0.0465</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="6">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-2.487704e-10</Numerator>
              <Numerator>4.73744e-09</Numerator>
              <Numerator>1.240319e-08</Numerator>
              <Numerator>2.18423e-09</Numerator>
              <Numerator>-2.973504e-08</Numerator>
              <Numerator>-2.774098e-08</Numerator>
              <Numerator>4.823501e-08</Numerator>
              <Numerator>9.04852e-08</Numerator>
              <Numerator>-4.377202e-08</Numerator>
              <Numerator>-2.029251e-07</Numerator>
              <Numerator>-2.93251e-08</Numerator>
              <Numerator>3.576771e-07</Numerator>
              <Numerator>2.380756e-07</Numerator>
              <Numerator>-5.050541e-07</Numerator>
              <Numerator>-6.566606e-07</Numerator>
              <Numerator>5.295136e-07</Numerator>
              <Numerator>1.333027e-06</Numerator>
              <Numerator>-2.353909e-07</Numerator>
              <Numerator>-2.234558e-06</Numerator>
              <Numerator>-6.431887e-07</Numerator>
              <Numerator>3.178848e-06</Numerator>
              <Numerator>2.391894e-06</Numerator>
              <Numerator>-3.766426e-06</Numerator>
              <Numerator>-5.213131e-06</Numerator>
              <Numerator>3.343879e-06</Numerator>
              <Numerator>9.069842e-06</Numerator>
              <Numerator>-1.034203e-06</Numerator>
              <Numerator>-1.349476e-05</Numerator>
              <Numerator>-4.128203e-06</Numerator>
              <Numerator>1.740814e-05</Numerator>
              <Numerator>1.293247e-05</Numerator>
              <Numerator>-1.901116e-05</Numerator>
              <Numerator>-2.55982e-05</Numerator>
              <Numerator>1.583847e-05</Numerator>
              <Numerator>4.129854e-05</Numerator>
              <Numerator>-5.051362e-06</Numerator>
              <Numerator>-5.769434e-05</Numerator>
              <Numerator>-1.597343e-05</Numerator>
              <Numerator>7.06232e-05</Numerator>
              <Numerator>4.876212e-05</Numerator>
              <Numerator>-7.411825e-05</Numerator>
              <Numerator>-9.265601e-05</Numerator>
              <Numerator>6.092806e-05</Numerator>
              <Numerator>0.0001437042</Numerator>
              <Numerator>-2.365713e-05</Numerator>
              <Numerator>-0.0001938177</Numerator>
              <Numerator>-4.346068e-05</Numerator>
              <Numerator>0.0002305286</Numerator>
              <Numerator>0.0001422997</Numerator>
              <Numerator>-0.0002376966</Numerator>
              <Numerator>-0.0002684195</Numerator>
              <Numerator>0.00019742</Numerator>
              <Numerator>0.0004089862</Numerator>
              <Numerator>-9.322642e-05</Numerator>
              <Numerator>-0.0005416667</Numerator>
              <Numerator>-8.56506e-05</Numerator>
              <Numerator>0.0006351459</Numerator>
              <Numerator>0.0003394235</Numerator>
              <Numerator>-0.0006517938</Numerator>
              <Numerator>-0.0006531623</Numerator>
              <Numerator>0.000552734</Numerator>
              <Numerator>0.0009935334</Numerator>
              <Numerator>-0.000305133</Numerator>
              <Numerator>-0.00130802</Numerator>
              <Numerator>-0.0001089867</Numerator>
              <Numerator>0.001527642</Numerator>
              <Numerator>0.0006836461</Numerator>
              <Numerator>-0.001573808</Numerator>
              <Numerator>-0.00138119</Numerator>
              <Numerator>0.001369316</Numerator>
              <Numerator>0.002127841</Numerator>
              <Numerator>-0.0008527391</Numerator>
              <Numerator>-0.002814326</Numerator>
              <Numerator>-5.435981e-06</Numerator>
              <Numerator>0.003302926</Numerator>
              <Numerator>0.001187235</Numerator>
              <Numerator>-0.003441493</Numerator>
              <Numerator>-0.002615018</Numerator>
              <Numerator>0.003083861</Numerator>
              <Numerator>0.004145541</Numerator>
              <Numerator>-0.002114933</Numerator>
              <Numerator>-0.005572669</Numerator>
              <Numerator>0.0004775432</Numerator>
              <Numerator>0.006640171</Numerator>
              <Numerator>0.001802538</Numerator>
              <Numerator>-0.00706464</Numerator>
              <Numerator>-0.004597381</Numerator>
              <Numerator>0.00656694</Numerator>
              <Numerator>0.007666904</Numerator>
              <Numerator>-0.00490895</Numerator>
              <Numerator>-0.01066029</Numerator>
              <Numerator>0.001931064</Numerator>
              <Numerator>0.01312888</Numerator>
              <Numerator>0.002414871</Numerator>
              <Numerator>-0.01454758</Numerator>
              <Numerator>-0.008042475</Numerator>
              <Numerator>0.01433728</Numerator>
              <Numerator>0.01472206</Numerator>
              <Numerator>-0.01187359</Numerator>
              <Numerator>-0.02208895</Numerator>
              <Numerator>0.00645106</Numerator>
              <Numerator>0.0296694</Numerator>
              <Numerator>0.002871719</Numerator>
              <Numerator>-0.03692219</Numerator>
              <Numerator>-0.01777635</Numerator>
              <Numerator>0.04329151</Numerator>
              <Numerator>0.04248361</Numerator>
              <Numerator>-0.04826485</Numerator>
              <Numerator>-0.09280869</Numerator>
              <Numerator>0.05142858</Numerator>
              <Numerator>0.3137774</Numerator>
              <Numerator>0.4474858</Numerator>
              <Numerator>0.3137774</Numerator>
              <Numerator>0.05142858</Numerator>
              <Numerator>-0.09280869</Numerator>
              <Numerator>-0.04826485</Numerator>
              <Numerator>0.04248361</Numerator>
              <Numerator>0.04329151</Numerator>
              <Numerator>-0.01777635</Numerator>
              <Numerator>-0.03692219</Numerator>
              <Numerator>0.002871719</Numerator>
              <Numerator>0.0296694</Numerator>
              <Numerator>0.00645106</Numerator>
              <Numerator>-0.02208895</Numerator>
              <Numerator>-0.01187359</Numerator>
              <Numerator>0.01472206</Numerator>
              <Numerator>0.01433728</Numerator>
              <Numerator>-0.008042475</Numerator>
              <Numerator>-0.01454758</Numerator>
              <Numerator>0.002414871</Numerator>
              <Numerator>0.01312888</Numerator>
              <Numerator>0.001931064</Numerator>
              <Numerator>-0.01066029</Numerator>
              <Numerator>-0.00490895</Numerator>
              <Numerator>0.007666904</Numerator>
              <Numerator>0.00656694</Numerator>
              <Numerator>-0.004597381</Numerator>
              <Numerator>-0.00706464</Numerator>
              <Numerator>0.001802538</Numerator>
              <Numerator>0.006640171</Numerator>
              <Numerator>0.0004775432</Numerator>
              <Numerator>-0.005572669</Numerator>
              <Numerator>-0.002114933</Numerator>
              <Numerator>0.004145541</Numerator>
              <Numerator>0.003083861</Numerator>
              <Numerator>-0.002615018</Numerator>
              <Numerator>-0.003441493</Numerator>
              <Numerator>0.001187235</Numerator>
              <Numerator>0.003302926</Numerator>
              <Numerator>-5.435981e-06</Numerator>
              <Numerator>-0.002814326</Numerator>
              <Numerator>-0.0008527391</Numerator>
              <Numerator>0.002127841</Numerator>
              <Numerator>0.001369316</Numerator>
              <Numerator>-0.00138119</Numerator>
              <Numerator>-0.001573808</Numerator>
              <Numerator>0.0006836461</Numerator>
              <Numerator>0.001527642</Numerator>
              <Numerator>-0.0001089867</Numerator>
              <Numerator>-0.00130802</Numerator>
              <Numerator>-0.000305133</Numerator>
              <Numerator>0.0009935334</Numerator>
              <Numerator>0.000552734</Numerator>
              <Numerator>-0.0006531623</Numerator>
              <Numerator>-0.0006517938</Numerator>
              <Numerator>0.0003394235</Numerator>
              <Numerator>0.0006351459</Numerator>
              <Numerator>-8.56506e-05</Numerator>
              <Numerator>-0.0005416667</Numerator>
              <Numerator>-9.322642e-05</Numerator>
              <Numerator>0.0004089862</Numerator>
              <Numerator>0.00019742</Numerator>
              <Numerator>-0.0002684195</Numerator>
              <Numerator>-0.0002376966</Numerator>
              <Numerator>0.0001422997</Numerator>
              <Numerator>0.0002305286</Numerator>
              <Numerator>-4.346068e-05</Numerator>
              <Numerator>-0.0001938177</Numerator>
              <Numerator>-2.365713e-05</Numerator>
              <Numerator>0.0001437042</Numerator>
              <Numerator>6.092806e-05</Numerator>
              <Numerator>-9.265601e-05</Numerator>
              <Numerator>-7.411825e-05</Numerator>
              <Numerator>4.876212e-05</Numerator>
              <Numerator>7.06232e-05</Numerator>
              <Numerator>-1.597343e-05</Numerator>
              <Numerator>-5.769434e-05</Numerator>
              <Numerator>-5.051362e-06</Numerator>
              <Numerator>4.129854e-05</Numerator>
              <Numerator>1.583847e-05</Numerator>
              <Numerator>-2.55982e-05</Numerator>
              <Numerator>-1.901116e-05</Numerator>
              <Numerator>1.293247e-05</Numerator>
              <Numerator>1.740814e-05</Numerator>
              <Numerator>-4.128203e-06</Numerator>
              <Numerator>-1.349476e-05</Numerator>
              <Numerator>-1.034203e-06</Numerator>
              <Numerator>9.069842e-06</Numerator>
              <Numerator>3.343879e-06</Numerator>
              <Numerator>-5.213131e-06</Numerator>
              <Numerator>-3.766426e-06</Numerator>
              <Numerator>2.391894e-06</Numerator>
              <Numerator>3.178848e-06</Numerator>
              <Numerator>-6.431887e-07</Numerator>
              <Numerator>-2.234558e-06</Numerator>
              <Numerator>-2.353909e-07</Numerator>
              <Numerator>1.333027e-06</Numerator>
              <Numerator>5.295136e-07</Numerator>
              <Numerator>-6.566606e-07</Numerator>
              <Numerator>-5.050541e-07</Numerator>
              <Numerator>2.380756e-07</Numerator>
              <Numerator>3.576771e-07</Numerator>
              <Numerator>-2.93251e-08</Numerator>
              <Numerator>-2.029251e-07</Numerator>
              <Numerator>-4.377202e-08</Numerator>
              <Numerator>9.04852e-08</Numerator>
              <Numerator>4.823501e-08</Numerator>
              <Numerator>-2.774098e-08</Numerator>
              <Numerator>-2.973504e-08</Numerator>
              <Numerator>2.18423e-09</Numerator>
              <Numerator>1.240319e-08</Numerator>
              <Numerator>4.73744e-09</Numerator>
              <Numerator>-2.487704e-10</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">200.0</InputSampleRate>
              <Factor>2</Factor>
              <Offset>0</Offset>
              <Delay>0.555</Delay>
              <Correction>0.555</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
        </Response>
      </Channel>
    </Station>
  </Network>
</FDSNStationXML>
