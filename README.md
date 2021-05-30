# Recruitment_agency
Backend REST API server serving as a "job candidates database"

### Python version
- [Python 3.8.6](https://www.python.org/downloads/release/python-386/)

### Packages
- Django 3.2.3
- Django REST framework 3.12.4

### Commands
#### First start
- Create the virtual environment for the project:
```shell
$ python3 -m venv venv
```
- Activate the virtual environment for the project:
```shell
$ source venv/bin/activate
```
- Update pip:
```shell
$ pip install --upgrade pip
```
- Install the requirements:
```shell
$ pip install -r requirements.txt
```
- CD into the project directory:
```shell
$ cd agency_project/
```
- Run migration. 
```shell
$ python manage.py migrate
```
- Run the application. 
```shell
$ python manage.py runserver