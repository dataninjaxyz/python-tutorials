# Python Virtual Environments

## What is a virtual environment?
A Python virtual environment is an isolated directory that contains a specific Python interpreter and its associated packages, allowing for project-specific dependency management without affecting the global Python installation or other projects.

- example
  - requests==2.20.0
  - requests==2.28.0

## Creating and using a virtual environment
```
$ python3 -m venv env
$ source ./env/bin/activate
(env)$ pip install requests==2.20.0
(env)$ pip list
```
venv is available in Python 3.3 and above
## Freezing and using requirements
```
   (env)$ pip freeze > requirements.txt
   (env)$ pip install -r requirements.txt
```