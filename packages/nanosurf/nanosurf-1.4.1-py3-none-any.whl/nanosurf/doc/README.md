# Introduction to Nanosurf Python library and application package

## Python API for Nanosurf controllers

Package for data acquisition and control of Nanosurf atomic force microscopes.

![Nanosurf Python](https://www.nanosurf.com/images/logos/nsf_python.png)

## Prerequisites

* Python >=3.9 installed on Windows OS.
* A Nanosurf controller software running and a controller connected to the PC.
* Nanosurf Scripting Interface option activated

## Installation and upgrading

Assuming that a Python interpreter is already installed on your PC.

To install the package, open a Windows Command Prompt and run:

```shell
pip install nanosurf
```

To upgrade your nanosurf package to the newest version,
open Windows Command Prompt and run:

```shell
pip install nanosurf -U
```

If for some reason pip does not work, unzip the content of the package
into a folder and in this folder run:

```shell
python setup.py install
```

## Get help, where are the examples ?

In the library, Nanosurf provides a documentation, some script demos and full fledged application templates to give you a quick start.
But where are these files placed after the installation?

They are in the nanosurf package sub folders "app" and "doc". 
But where are they on your system?

Depending on the exact installation of python, the package folders can be at very different places.

Therefore, the nanosurf package provides a command shell script to help you:

Open Windows Command Prompt and type:

```shell
nanosurf_help
```

The output of this command print the exact path to the app and doc folder.
Use this path to open the example scripts in Visual Studio Code (or any other python IDE) and run them.

If this shell script does not run you can do it manually:
Open Windows Command Prompt and type:

```python
python 
>>> import nanosurf
>>> nanosurf.help()
```

Open the examples in Visual Studio Code (or any other python IDE) and run them

## Usage Example

```python
import nanosurf as nsf

spm = nsf.SPM()  # or .C3000() or .CX(), or .CoreAFM()
application = spm.application

scan = application.Scan
opmode = application.OperatingMode
approach = application.Approach
zcontrol = application.ZController
head = application.ScanHead

# Set file mask
mask = "TestSample-"
application.SetGalleryHistoryFilenameMask(mask)

# Choose cantilever
head.CantileverByGUID = spm.CantileverGUID.Dyn190Al

# Operating mode
opmode.OperatingMode = spm.OperatingMode.DynamicAFM
opmode.VibratingAmpl = 0.5 # [V] 

# Set scan parameters
scan.ImageWidth = 5e-6 # [m]
scan.ImageHeight = 5e-6 # [m]
scan.Scantime = 0.55 # s
scan.Points = 256 # points per line
scan.Lines = 256 # lines
scan.CenterPosX = 10e-6 # [m]
scan.CenterPosY = 10e-6 # [m]
scan.SlopeX = 0.0 # degree
scan.SlopeY = 0.0 # degree
scan.Overscan = 5 #%

# Set Z controller parameters
zcontrol.SetPoint = 70 # [%]
zcontrol.PGain = 3100
zcontrol.IGain = 3500

# Start scan
scan.StartFrameUp()

# Check if scanning
scanning = scan.IsScanning
print(scanning)

# Stop scan
scan.Stop()

# Get image
scan.StartCapture()

del spm

```

## Scripting Manual

Full list of objects and methods can be found in the Scripting Manual
in Nanosurf controller software under Help tab:
Help -> Manuals -> Script Programmers Manual, or [here](https://www.nanosurf.com/downloads/programmers-manual.pdf).

## Library Version History

* v1.4.1
  * bugfix: Studio vector attributes are defined as .vector instead of .value
  * improve installation instruction for editable mode

* v1.4.0
  * Add enum support for Nanosurf Studio scripting interface
  * Nanosurf Studio properties and LogicalUnits attributes have common interface style
  * Add revers ramp feature to App_Switching_Spectroscopy
  * Some small improvements to other applications

* v1.3.4
  * fix bug in frequency_sweep

* v1.3.3
  * Improve visual appearance of some nsf.gui elements
  * fix eeprom memory write access for i2c.chip_24LC34A
  * better return value for fileutil.create_unique_folder() in case of error

* v1.3.2
  * Bugfix: Studio - handling of boolean properties was not working
  * Add support for DriveAFM Camera i2c-chip

* v1.3.1
  * Bugfix: App_switching_spectroscopy - selection of output and amplitude setting had some issues

* v1.3.0
  * Add simplifies library usage is possible. Just write 'import nanosurf as nsf' and full access to sub-libraries is provided in visual studio code
  * new app: app_switching_spectroscopy provides the possibility to measure in "Switching Spectroscopy"-Mode
  * new qui elements: nsf.gui.NSFEdit and nsf.gui.NSFComboBox
  * Bugfix: Wrong number type in Python for double based property   
  * Bugfix: nsf.spm.workflow.frequency_sweep: PositionX/Y/Z was not working as output

* v1.2.0
  * Add Studio scripting support

* v1.1.0
  * Add direct I2C motor control

* v1.0.0
  * Initial release

### License

[MIT License](https://en.wikipedia.org/wiki/MIT_License)
