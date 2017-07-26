# Stock Management
Application to Manage Stock Datas, like Opening prices, Closing prices. The application calculate the Percantage Change of Individual Company Shares.

# About
This is the Python Django Application to manage Stock Management. To get started, please see the below steps.

#The things need for installation
The Machine which support Python 2.x versions

# Installation
1). Clone the application using clone URL.
`git clone url`

2). Create a virtual environment. Using the command (virtualenv ~"name" ). And activate the Virtualenv.
To create virtualenv use `virtualenv` and activate `source virtualname/bin/activate`:

 3). Run the requirement package.

```bash
$ pip install -r requirements.txt
```
 4). Run the migration steps.
 
 ```bash
$ python manage.py makemigration
$ python manage.py migrate
```
 5). Run the application.
 
 ```bash
$ python manage.runserver 0.0.0.0:8000


# Python Version
Python 2.7, 3.4 are fully supported and tested.


#Technologies 
: Python 2.x, Django 1.11.3, pytz==2017.2


