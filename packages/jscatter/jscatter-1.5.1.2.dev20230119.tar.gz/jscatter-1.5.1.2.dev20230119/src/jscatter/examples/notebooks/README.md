# Jscatter

The notebook directory contains some introductory files similar to the 
BeginnersGuide in the HTML documentation.

- Jscatter_Introduction.ipynb
- Jscatter_ReadData.ipynb
- Jscatter_BuildModels.ipynb
- Jscatter_Fitting.ipynb
- Jscatter_Lattice.ipynb
- Jscatter_Template.ipynb     
- Jscatter_Jupyterinstallation.ipynb

The main content about existing models and all options of specific commands
is found at [Jscatter](https://jscatter.readthedocs.io/en/latest/index.html)
including installation instructions.

Jupyter is a nice tool for demonstration, first learning and fast running evaluations. 
For strong usage with models that may take some time for calculation 
and fitting it is easier to use a command shell on Linux/OSX or even Windows. 
The shell can be put into background or on a cluster you can 
detach a shell running screen to later reconnect (there should be no graphical output).

For Jupyter the needed matplotlib is somehow slow that 
during the fit not updated output is possible (but works).

The notebooks contain a header section that installs Jscatter on a read only server.
If you run the notebooks on your local computer Jscatter may be installed
once as explained in one notebook. 
Then you need only to import Jscatter and NumPy.
