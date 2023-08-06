# ecalic package

This package handles CMS Ecal Intercalibration Constant (IC) and IC-like operation and visualisation.
This applies to several type of Ecal conditions which have a value per crystal, for example:
- EcalIntercalibConstantsRcd
- EcalLaserAPDPNRatiosRcd
- EcalChannelStatusRcd
- EcalPedestalsRcd (pedestal or rms)

The package contains two modules:
- `ecalic.iov` decodes ecal conditions (xml format)
- `ecalic.ic` the main module

To install the package one needs (automatically installed)
```
pip install --user ecalic
```

All the examples below were tested in `ipython`, to try them:
- install ipython
```
pip install --user ipython
```
- start by typing `ipython`
- copy-paste the block of commands

Documentation (in ipython):
```
import ecalic as ecal
help(ecal)
```

## ecalic.iov

Use this module to decode an xml file downloaded from the database.
The example (the commands can be run in `ipython`) below will transform a pedestal xml file
in a txt file format (`ix iy iz ic`) where `ic` is the pedestal RMS in gain 6

```
import ecalic as ecal

### for python2 python3 compatibility
try:
   from urllib.request import urlopen
except ImportError:
   from urllib2 import urlopen

### input files
www = 'https://ecaldpg.web.cern.ch/ecaldpg/users/fcouderc/examples/ecalic/'
pedestal_file =  urlopen(www + '/pedestals_hlt_run324773.xml' )
i = ecal.xml( pedestal_file, type = 'noise6' )

### dump to a txt
i.dump_txt('noise_gain6.txt')

### or directly as icCMS
ic = ecal.xml( pedestal_file, type = 'noise6' ).icCMS('noise Gx6')
```
The available types `type` can be found in the help
```
? ecal.xml
```

## ecalic.ic

This is the heart of the package. It contains:
- the class `icCMS` which represents the IC
- the `geom` variable which handles all the different crystal properties (pandas DataFrame)
- the function `icCovCor` to get the correlation and covariance between different IC sets.


A first simple example to see and plot crystal properties
```
import matplotlib.pyplot as plt
import ecalic as ecal

### activate pyplot visualisation
plt.ion()
plt.show()

### dump the properties of 2 first crytals
ecal.geom.head(2)

### define an empty icCMS instance
i = ecal.icCMS()

### plot the FED in 2D
i.plot(var= 'FED', title = 'FED number')

### plot the crytal type (BTCP or SIC)
i.plot(var='fabric', title = 'producer')

### EB plot only
i.plot(var='fabric', title = 'producer',ecalpart = 'eb')
```
Note that the `cmsStyle` package is provided for plot polishing and is not mandatory.

The different methods from the `icCMS` class can be found:
```
help(ecal.icCMS)
```

### use-case example

In this example we do some simple `ecalic.ic` operations.
First, download an example file:
```
try:
   from urllib.request import urlopen
except ImportError:
   from urllib2 import urlopen

### getting the example txt file from the web
www = 'https://ecaldpg.web.cern.ch/ecaldpg/users/fcouderc/examples/ecalic/'
inputtxt = urlopen(www + '/ic_example.txt')
with open( 'ic.test.txt','wb') as ftest: ftest.write(inputtxt.read())
inputtxt.close()
```

And try the commands:
```
import ecalic as ecal

###create an instance of ecalic.ic
i =  ecal.icCMS( 'ic.test.txt' , 'example IC' )

### help for each method
?i.etaRingNorm

### normalize to 1 per eta ring
i.etaRingNorm()

### plot 2D
i.plot( zRange_eb = [0.98,1.02], zRange_ee = [0.95,1.05], title = 'IC test'  )

### average per harness and plot,
### remove 10% of the most tailish cristals (left and right from mean)

# add a variable with the average
# trim = remove 10% of the most tailish cristals (left and right from mean)
i['ic_av'] = i.average( groupby='harness', trim = 0.10 )
# plot the average
i.plot( var = 'ic_av', zRange_eb = [0.98,1.02], zRange_ee = [0.95,1.05], title = 'IC test average'  )
ecal.plt.show()
```


### A more involved example
In the following example we will:
- get the noise (in gain 12) from two different runs (xml included in the package)
- get the corresponding channel status
- mask the bad channel in the noise ics
- plot the noise in 2D
- profile these noise along `ieta`
- get the correlation between the 2 ics

Get the example script at [testNoise.py](https://gitlab.cern.ch/cms-ecal-dpg/ecalic/raw/master/ecalic/test/testNoise.py?inline=false)

And run the script
```
python testNoise.py
```
