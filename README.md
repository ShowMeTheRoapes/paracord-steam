# Paracord Steam

## Dependencies: 
- Python 3.8.1
- venv

## Virtual Environment: 
It will be easiest to set up a virtual environment to work out of. Follow [these steps](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment) to set it up.
Dont forget to activate and deactive the virtual environment when working/leaving this project.

#### PyCharm Setup
To have PyCharm use the correct environment and dependencies, you need to configure the virtual environment. 
- Go into the project settings Project:paracord-steam > Project Interpreter.
- Click on the gear icon next to the interpreter and add a new one. 
- Select "Existing Environement" bullet and select the python.exe file that lives in the venv directory you created.
- Click OK and you dependencies should start showing up in the interpreter dependency view.

## Package Management
Pip has a feature for importing a list of packages from a file. We will use this to keep our virtual environments up to date with the project. Copy any new prod dependencies and versions into the `requirements-prod.txt` file and any test dependencies into the `requirements.txt` file. To install all listed dependencies for a local dev environement run `pip install -r requirements.txt`. If you ever want to uninstall the dependencies installed by the requirements file, a `pip uninstall -r requirements.txt` should do the trick.
