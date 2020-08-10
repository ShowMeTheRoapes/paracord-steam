# Paracord Steam Server

## Dependencies: 
- Python 3.8.1
- venv

## Virtual Environment: 
It will be easiest to set up a virtual environment to work out of. Follow [these steps](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment) to set it up.
Dont forget to activate and deactive the virtual environment when working/leaving this project.

#### PyCharm Setup Venv
To have PyCharm use the correct environment and dependencies, you need to configure the virtual environment. 
- Go into the project settings Project:paracord-steam > Project Interpreter.
- Click on the gear icon next to the interpreter and add a new one. 
- Select "Existing Environement" bullet and select the python.exe file that lives in the venv directory you created.
- Click OK and you dependencies should start showing up in the interpreter dependency view.

#### PyCharm Docker
To have pycharm use the correct environment and dependencies from a docker container, you need to first run one of the docker-compose commands below to create the proper images. (May be PyCharm Professional only)
- Go into the project settings Project:paracord-steam > Project Interpreter.
- Click on the gear icon next to the interpreter and add a new one. 
- Select "Docker"
- If nothing is showing up in the "Server" dropdown, click "New.."
    - Windows: Use TCP socket with "Engine API URL" of "tcp://localhost:2375". You will need to enable this way of connecting in your docker desktop settings.
    - Mac: Use the option with Mac in the name
    - Linux: Google it
- From the image dropdown select one similar to "uat_server_local:latest"
- Click OK and you should be redirected to a view that will load your dependencies.

Now you should be able to run files like normal and you dont even need python on your machine!

## Package Management
Pip has a feature for importing a list of packages from a file. We will use this to keep our virtual environments up to date with the project. Copy any new prod dependencies and versions into the `requirements-prod.txt` file and any test dependencies into the `requirements.txt` file. To install all listed dependencies for a local dev environement run `pip install -r requirements.txt`. If you ever want to uninstall the dependencies installed by the requirements file, a `pip uninstall -r requirements.txt` should do the trick.

## Helpful commands
From the `server` directory you can run the following commands:
* If you want to run the unit tests:
    1. `docker-compose -f docker\dev\docker-compose.yml build` to build a docker container for meant for testing the service. 
    2. `docker-compose -f docker\dev\docker-compose.yml up` to run all the unittests in the project.
* If you want to run an entire dockerized local test suite:
    1. `docker-compose -f uats\docker-compose.yml build` to build all the images related to a local uat test (a local service container and a container for running the uats). 
    2. `docker-compose -f uats\docker-compose.yml up` starts the containers and runs the tests 
* If you just want to run the service container, run these commands:
    1. `docker-compose -f uats\docker-compose.yml build local_steam_server`
    2. `docker-compose -f uats\docker-compose.yml up local_steam_server`
* If you want to clean up the artifact from one of the previous runs:
    1. `docker-compose -f {location of compose file} down`
* A shorthand for running both the build and up commands is doing `docker-compose -f {location of compose file} up --build`


From anywhere you can run:
* `docker container prune` to clean up all stopped containers.
* `docker image prune` to clean up all unused docker images.
* `docker system prune -a --volumes` to clean up most of the docker artifacts on the system.
