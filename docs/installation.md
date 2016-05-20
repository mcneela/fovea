# Installation

## General

### Dependencies
Fovea has been tested for compatibility with both Python 2.7+ and Python 3.4+
Polygon domain functionality (domain2D) depends on shapely 1.2+ and descartes 1.0.1+
The Bombardier example depends on YAML (via PyYAML)

The dimensionality reduction examples require the Modular Toolkit for Data Processing (MDP). This can be installed by running `pip install MDP`.

All underlying dynamics are solved using [PyDSTool](http://github.com/robclewley/pydstool).

Other dependencies are as follows:

* PyYAML 3.11 or greater
* StructLog 15.1 or greater
* TinyDB 2.0 or greater
* Euclid 0.01 or greater
* Matplotlib 1.5.0 or great
* Numpy (Installed with PyDSTool)
* Scipy (Installed with PyDStool)

### Install
Run `python setup.py install` from the downloaded folder.

## Windows

## Mac

## Linux
*This install procedure has been tested on Ubuntu 14.04 LTS*

On Linux, a number of library packages are required for building and
installing Fovea's various dependencies. To avoid build errors stemming from
issues with the way in which setuptools attempts to build packages from
source, consider installing as follows:

    virtualenv venv		# Create a virtual environment for Fovea and dependencies
	source venv/bin/activate    # Activate the virtual environment
	pip install numpy
	pip install scipy
	pip install matplotlib
	pip install pydstool
	python setup.py install fovea

Next, you will need to configure Matplotlib such that it uses an interactive
backend allowing for the dynamic viewing of figures and plots. To do this 
you will need to edit your Matplotlibrc file. If you're using virtualenv, 
this file can be found in `/venv/lib/pythonX.Y/site-packages/matplotlib`
where pythonX.Y is your Python version (e.g. python3.4). If you installed
Matplotlib globally, your Matplotlibrc can be found in `~/.config/matplotlib`

Now, open the Matplotlibrc file and find the option for specifying the backend. By default, it will be set to Agg which does not allow for the
displaying of or interaction with plots and figures. Specify an interactive
backend such as GTK3Agg, TkAgg, or WXAgg. Some of these backends are
specific to either Python 2 or Python 3, so please consult the Matplotlib
[website](http://matplotlib.org/faq/usage_faq.html#what-is-a-backend) before
choosing a backend.

Your Fovea installation should now be complete. To test that everything is
working properly run
	
	python
	>>> import fovea
	
and then try running some of the examples given in the examples folder.
