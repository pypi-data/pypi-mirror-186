[![Build Python application](https://github.com/abulgher/autologbook/actions/workflows/python-app.yml/badge.svg)](https://github.com/abulgher/autologbook/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/abulgher/autologbook/actions/workflows/python-publish.yml/badge.svg)](https://github.com/abulgher/autologbook/actions/workflows/python-publish.yml)
[![PyTest](https://github.com/abulgher/autologbook/actions/workflows/pytest-app.yml/badge.svg)](https://github.com/abulgher/autologbook/actions/workflows/pytest-app.yml)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)

# AUTOLOGBOOK

A python toolkit for the automatic generation of elog entries of SEM analysis.

## Features

- Set a **watchdog** to keep monitoring the status of a project folder. Every new image added to the folder is
  automatically included in the logbook.
- The script can automatically recognize the origin of the TIFF images. If coming from a FEI/Thermofisher microscope
  then the specific tags are decoded and included in the logbook.
- A thumbnail png and a full size png copy of all images are also created in order to have easier access from
  web-browser.
- It connects to the JRC eLog server where the automatically generated protocol entry is uploaded.
- Mirroring option. It is common to have microscope pictures saved locally on the microscope PC and also mirrored on a
  remote computer. In order for the autologbook to work, the project folder must be on a specific network share that is
  reachable by the web-server. To facilitate this task, the user can save the images locally and, if the mirroring
  option is activated, they will be copied directly to the remote data-server.

## The protocol

It is a hierarchical objects including several dedicated containers for similar objects. All dependent objects are
automatically added during the execution of the watchdog and can be customized by the user via the Protocol Editor.

The typical structure of a protocol is the following:

- Introduction:
  - A textual section that the user can customize with a description of the experiment. It will be rendered in the HTML
    output if and only if it is not empty.
- General optical images:
  - It is a list optical microscope or generic digital pictures of interest for the experiment, they could represent
    for example the container with which the samples were delivered and so on.
  - In order to have an optical image in this section, the user has to put in the base folder of the protocol.
  - This section will be rendered, only if at least one project level optical image is present.
  - Each optical image can be customized via the protocol editor with three fields, *caption*, *description* and
    *additional information*.
- Samples:
  - This section can be customized adding a general description of all samples in the protocol.
  - Each sample and subsample can as well be customized with a specific description.
  - Every sample corresponds to a sub-directory in the base folder of the protocol.
  - Each sample is also having a hierarchical structure with subsamples and containers for its elements. In particular,
    there are four containers:
    - Microscope pictures (generally TIFF files)
    - Videos (generally mp4 files)
    - Optical images (generally jpeg and png files)
    - Attachments (generally pdf and doc files.)
  - All elements of a sample can be customized.
- Conclusion:
  - Similarly to the introduction, it is a pure textual section with no corresponding files. It will be rendered in the
    HTML output only if it is not empty.
- Attachments:
  - A list of project wide attachments.

It is recommended to subclass the base ELOGProtocol to cope the specificity of each microscope.

### The inheritance tree of the Protocol

As said above, the basic Protocol is an almost empty class which cannot be used directly. It is meant as a prototype for
all possible ways an analysis protocol can be implemented.

It's first daughter class is the **ELOGProtocol**, that is actually implementing the possibility to transfer its content
to a running eLog server. This is accomplished thanks to the ``elog`` package provided
by [PSI](https://github.com/paulscherrerinstitute/py_elog).

Going down the derivative tree we find the **QuattroELOGProtocol**. This is a specialization of the *ELOGProtocol*
because it includes the handling of navigation pictures that other microscopes do not have. The **VersaELOGProtocol** is
another specialization of the *ELOGProtocol* very similar to the QuattroELOGProtocol but for the navigation images that
are not present. There are subclasses for the XL40 and Vega microscopes as well.

### The inheritance tree of the MicroscopePicture.

In a similar way we have an inheritance tree for the **MicroscopePicture**.

#### FEIPicture for FEI Microscopes

It's first daughter is the **FEIPicture** where the specific FEI tags are read from the file and some relevant image
parameters are then added to the microscope picture and included in the generated protocol.

Subclassed from the *FEIPicture*, we have the **QuattroFEIPicture** and the **VersaFEIPicture** where the ID is
retrieved from the file name if it follows a standard naming convention. Moreover, there are two optional image
treatments that can be applied on the fly while a FEIPicture is added to the protocol, it is to say the **automatic
calibration** and the **automatic databar removal**.

- **Automatic Calibration**. In fact, in TIFF files generated by FEI microscopes the resolution values encoded in the
  basic TIFF Tags that are used by common imaging software (like *ImageJ*) to calibrate the picture are wrong (always
  set to 28 x 28 dpi), even if all the required information to perform the calibration is available in the FEI specific
  TAG sets. Activating the option for automatic calibration (either from the configuration file or from the
  configuration editor window), the wrong values are replaced with the correct ones, so that all images will be stored
  on the image server already calibrated for further use. This option is turned **ON** by default.
- **Automatic Databar removal**. Similarly, it is also possible to crop the image on the fly in order to remove the
  databar. Differently from the calibration, here the cropped image is saved in a separated file (inside a *crop*
  folder with also a *_crop* in the filename). This is done in order to avoid important data lost. One can access the
  cropped images directly from the logbook web page. This option in turned **OFF** by default in order to avoid
  overloading the storage capability.

#### VegaPicture for the TESCAN Vega microscope

A subclass of the MicroscopePicture being used for the Vega Tescan microscope. Differently from the FEI systems, this
system is saving two files (a TIFF image and also plain text metadata file). The same metadata are also encoded in the
TIFF file and can be parsed. The plain text file is anyhow copied to mirroring folder in case the final user wants to
read it.
The microscope software can save the images in two formats: **TIFF** (recommended) and **JPEG**. For TIFF files, it is
possible to perform automatic image calibration, using the metadata information. For JPEG files, since no information
can be written in the file, it makes no sense to perform any image pre-treatment.

#### XL40Picture for the Philips microscope

A subclass of the MicroscopePicture being used for the XL40 Philips microscopes. This is kind of special because the
metadata are stored in XMPMETA xml format and, even more, complex is the handling of multi-page tiff files (one page for
the SE and one for the BSE).
As for other subclass, it is possible to automatic calibrate the TIFF file. No databar crop is possible since the
additional information are printed on top of the image itself.

## Protocol editor and customization

The role of the autologbook package is to build a protocol for the analysis session. The automatic procedure is sorting
all acquired elements (navigation and microscope pictures, videos, sample and subsamples, pdf reports...) in a standard
form, but the microscope operator or the final user may want to customize the protocol comments adding some extra
information. The best way would be to edit the output HTML page directly on the ELOG server, but this is not possible
during the analysis itself, because as soon as a new element is added to the protocol, autologbook will regenerate the
complete HTML content and replace it with the existing one on the server. In other words, all modifications made on the
HTML directly on the ELOG page while the autologbook watchdog is running, will be sooner or later lost.
A possible solution is to wait until the end of the analysis session before starting doing all the customizations, but
this is for sure not really practical.
The solution adopted by the autologbook is to let the user customize his protocol via the ``ProtocolEditor`` dialog. It
is activated during the execution of the watchdog by pressing the corresponding push button on the main window.
The protocol editor window is featuring three columns, on the left side a tree view widget where the protocol structure
is shown along with a list view where only elements contained in the selected sample are displayed. These two views are
synchronized, so when an element is selected on one view, it is also selected on the other. By selecting an element on
these two views, all fields in the central and right part of the window are updated. In the central area, there is a
preview frame where images and videos can be displayed along with a tabular view where the selected item metadata are
listed.
Three customization fields are available for the user on the right side: the **caption** (available only for images and
videos), the **description** and the **extra information**. The information inserted into these fields are passed to the
yaml customization file and consequently to the logbook.

## Configuration settings

All parameters allowing the proper functioning of the tool can be configured either via a configuration file or directly
in the GUI via the ConfigurationEditorDialog.
The configuration file (\*.ini) is parsed with the ``ConfigParser`` module.
If started on the command line, the user can select which configuration file to use by using the option *-c* or
*--conf-file*.

An experiment file (\*.exp) is also a configuration file where an additional section ``'GUI'`` is added and that
contains all the values of the various widgets. In this way the same protocol can be regenerated in a few mouse clicks.

# Installation

Installation of the **AUTOLOGBOOK** is extremely easy and it is based on ``pip``. The procedure to follow is slightly
different if you intend to just to use the package or if you want to work on its development.
Both approaches are described here below.

## Ready to use installation

If you follow this procedure you won't be able to modify the package source and you will just use it as it is or include
it in your package as a library.
The best approach is to isolate all your installations in a separate enviroment so not to corrupt any other working
tools.
```bat
rem Generate a fresh environment
python -m venv autologenv
cd autologenv
rem Activate the enviroment
Scripts\activate.bat
rem Just install latest autologbook version from PIP
pip install autologbook
```

For running, autologbook needs that a few dependencies to be fulfilled. You don't have to worry about this because pip
is taking care of the task, but here below a list of requirements is reported just for you to know.

### Requirements

The autologbook package has been developed with python 3.10.5 In principle, it should be working also with other
versions, but it was never tested.
Here is a list of the most important packages needed for execution of the autologbook.

- py_elog v1.3.15 --> To interface to the ELOG server. Please have a look at this [note](#elog-note).
- PyQt5 v5.15.7 --> The GUI.
- Markdown v3.4.1 --> To format the custom HTML content.
- watchdog v2.1.9 --> To automatize the mirroring process and the addition of new elements to the protocol.
- tenacity v8.0.1 --> To stabilize the watchdog execution against intermittent problems and network overloads.
- Pillow v9.2.0 --> To manipulate images.
- PyYAML v6.0 --> To store custom protocol information.
- defusedxml v0.7.1 --> To read xmpmeta data from XL40 images
- piexif v1.1.3 --> To easily manipulate EXIF metadata for JPEG.
- jinja2 v3.1.2 --> To render the HTML output.
- yammy v0.5.4 --> To easily edit jinja2 templates

The complete list of requirements is included in the requirements.txt file distributed with the package. However, if the user decides to install ``autologbook`` via ``pip`` [link](#ready-to-use-installation), the installation procedure will take care of installing all needed dependencies.

#### ELOG note
A minor bug fix has been included in the latest master branch of the py_elog package. This is to avoid double attachment uploads for files with blanks in the filename. This bug fix will be released with the next py_elog release (1.3.16), but until this will be available, just build the source.

## Install in development mode
Pip allows you to install a package in development mode so that you can have it install in your environment but at the same time you can keep to modify its source.
Here is a simplified procedure.
```bat
rem Generate a fresh environment
python -m venv autologenv
cd autologenv
Scripts\activate.bat
rem Get the source code from GitHub
git clone https://github.com/abulgher/autologbook.git
rem Install the requirements for development purpose
pip install -r autologbook\requirements-dev.txt
rem Install the package in development mode
pip install -e autologbook
```

## Execution
To run the autologbook module you just need to activate your python enviroment and enter the commands as here below.
```bat
rem Create a dedicated enviroment if you don't have it already
py -m venv myenv
cd myenv
rem Activate your python enviroment
Scripts\activate.bat
rem Install the autologbook module
pip install autologbook
rem Start the GUI
python -m autologbook
```

Using ``python -m autologbook -h``, you can get a list of command line options and flags to be used.

Another possibility is to use the executable file that is generated during the building process. This can be found in the Script folder of your python enviroment. Type from a cmd shell ``autologbook-gui.exe`` or just double-click on it to get started.

# The ELOG counterpart
autologbook is posting logbook entries to ELOG and while the connection details (hostname, port, username...) and the microscope specific logbook are parameters that can be adjusted by the user via the configuration file, the logbook structure is hardcoded and cannot be modified without having to recode a large fraction of the code.

The expected logbook structure is shown in this image:
![elog-counterpart](https://user-images.githubusercontent.com/12378877/188565458-fa8df239-5ffd-4dd1-bcc4-60b2cee520f1.PNG)

When creating a dedicated logbook for a microscope to be used with autologbook, its structure must reflect this image and can also be copied from this elog configuration file snippet:
```
Theme = default
Comment = Logbook of Quattro analyses
Time format = %Y-%m-%d %H:%M:%S
Date format = %Y-%m-%d
Display mode = summary
Summary lines = 0
Reverse Sort = 1

;------------- Define here all the attributes -------------------
Attributes = Operator, Creation date, Protocol ID, Project, Customer, Edit Lock
Required attributes = Operator, Protocol ID, Project, Customer


;---------- OPERATOR
Preset Operator = $long_name
Subst Operator = $long_name

;---------- CREATION DATE
Type Creation date = date
Preset Creation date = $date

;---------- Protocol ID
Comment Protocol ID = Please provide the numeric digits of the protocol

;---------- Project
Comment Project = Please provide the project name (usually the second part of the folder name)

;---------- Customer
Comment Customer = Please provide the customer name (usually the third part of the folder name)

;---------- Edit Lock
ROptions Edit Lock = Protected, Unprotected
Preset Edit Lock = Unprotected
Comment Edit Lock = Use this switch to protect the entry against accidental automatic editing.


List display = ID, Creation date,  Operator,  Protocol ID, Project, Customer
Link display = ID
Quick filter = Protocol ID, Project, Customer
```
## The Edit Lock
Starting from release v0.0.1.b.1, an Edit Lock flag has been introduced in the eLog structure. This is meant to protect an elog entry from accidental automatic editing. For example, after an elog entry has been generated with the autolog, the user decided to customize its content using the web editor interface instead of the Protocol Editor GUI. If the autologbook watchdog will be started again in the same folder, the standard HTML protocol will be generated and will replace the user customized one. In order to protect against this automatic re-editing, the user can set the Edit Lock to **Protected** and the autologbook will consider this entry as read-only.

When a read-only entry is found, the user is asked to decide what to do, (s)he may want to override the read-only flag regenerating the HTML content from the original protocol content, or to back up the read-only entry and generate a new one for the current protocol, or, as a last option, to change the protocol identification number for the current experiment.

**WARNING**. The check of the read-only flag is performed only before the watchdog is started. This means that if the user is protecting the entry while the watchdog is still running, this will be totally ignored.

# The experiment wizard

Creating a new experiment from scratch can be tough and error-prone. In particular, you may not remember what is the
right (and unique) protocol number to be used. The easiest way is to start the experiment wizard and let it guide you in
the process.
You can use this tool for creating a brand-new experiment from scratch or to continue an existing experiment. In both
cases, the wizard will exchange information with the microscopy protocols list and either download or prepare the
experiment file for the user.

To start the experiment wizard is included in the standard installation. You just need to start it either by
launching ``experiment-wizard.exe`` from the Script folder of your python enviroment or simply double-clicking on it.

# The labtools
Along with the main automatic logbook generation, the package comes with a series of useful labtools executables (mainly CLI, but also GUI). Those executables will be available in the Scripts directory of your virtual enviroment.
