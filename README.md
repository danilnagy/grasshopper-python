# grasshopper-python

This is a template for creating a connection between a Grasshopper definition and a Python script that must run externally. This is particularly useful for itegrating Python scripts within your Grasshopper definitions that rely on libraries which are not included with core Python (and thus are difficult or impossible to use with Grasshopper's IronPython 2.7). The only dependency is to have whatever version of Python you want to use to run your external script installed on your system.

1. Open requirements.txt and add any Python libraries your script depends on. These will be installed when we create the Python environment in the next step.
2. Run `install.bat` to create the Python environment with the proper dependencies. If you don't run this, it will be run the first time you execute the Grasshopper definition.
3. Open the `grasshopper.gh` file in Grasshopper. The Python component in the Grasshopper definition will execute the `python.py` script and return any data generated.