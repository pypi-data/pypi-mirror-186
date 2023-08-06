# PySimulationEngine
Python Library to run a simulation with user objects and AIs and display it all through a simple GUI.

### Active Env
> source venv/bin/activate

### Testing
> python setup.py pytest

will execute all tests stored in the ‘tests’ folder.

### Build Library
Now that all the content is there, we want to build our library. Make sure your present working directory is /path/to/mypythonlibrary (so the root folder of your project). In your command prompt, run:
> python setup.py bdist_wheel

### Install Library
> pip install /path/to/wheelfile.whl
> pip install dist/PySimulationEngine-0.1.0-py3-none-any.whl --force-reinstall --config-settings --confirm-license= --verbose --no-deps PyQt5

### Additional Information
PyQT5 can be installed by:
> pip install pyqt5 --config-settings --confirm-license= --verbose