# Survey API

Survey API is written in Python and uses the Flask webframework to provide endpoints to interact with a MongoDB database.

The database has surveys and survey_response collections.

New entries for survey responses can be added provided that the maximum number of respondents has not been exceeded.

## Installation

Python3.7 is required.

MongoDB is required for this project. [Installation guides](https://docs.mongodb.com/manual/administration/install-community/)

* Run MongoDB locally (your command may be different depedning on where MongoDB is installed)
```
mongod
```

* Create a python virtual environment

```
pip install -m venv your_virtual_environment_name
```

* Activate your virtual environment

On Mac OS

```
cd your_virtual_environment_name
source bin/activate
```

On Windows

```
cd your_virtual_environment_name
Scripts\activate
```

* git clone the project to your local machine

* install requirements from inside the git repository

```
pip install -r requirements.txt
```

## Testing

Use nose2 to run unit tests

```
nose2
```

## Run the Application

On Mac Os

```
export FLASK_APP=run.py
flask run
```

On Windows

```
set FLASK_APP=run.py
flask run
```
