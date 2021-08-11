# networksimulation

Purpose of this repository is to further research on networks. The original author of this rep is "https://github.com/Braudt". The same license as the original is added to the rep. 

Any changes made to the original here are only for research experimentation. The steps below show minor changes made to the original codebase.

The commands below should work on mac and linux systems (might not always work on windows), conda users have similar commands refer to conda guide.

Setup
-----
* Download Python 3.7.3 (version link: https://www.python.org/downloads/release/python-373/)
* Install the Python version
* git clone "repo link" (before cloning go to the desired directory where you would like to clone)
* Open your desired IDE (vscode, pycharm, etc) -> open the folder that is cloned
* Go to terminal inside the IDE (where python is enabled)
* Type the following commands to setup the environment and install required libraries.

```
$ virtualenv venv --python=python3.7.3
```
  - (creates python virtual environment of version 3.7.3)
```
$ source venv/bin/activate
```
  - (activates the venv)
```
$ pip install -r requirements.txt
```
  - (installs all libraries in requirements.txt)

* Run the main.py file (or type ./test.sh in terminal)

Output
------

The "main.py" executes all the files which run experiments(generate PDF and saves results of output by the same name of the .py files). All results in output logs will be appended in their respective .txt files. Although new PDF will be generated each time the "main.py" is executed.

Issues
------
* Make sure your python version is installed and its environmental variables are set and are visible in IDE.
* To ensure correct python version is running and installed in virtual environment (type: python -V or python --version) in terminal inside IDE after activating virtual environment
* First time python users install any python plugins in respective IDE (if needed)
