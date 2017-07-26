Stock Management

Application to Manage Stock Datas, like Opening prices, Closing prices.
The application calculate the Percantage Change of Individual Company Shares.

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
Prerequisites

What things you need to install the software and how to install them

The Machine which support Python 2.x versions

Installing

1). Clone the application using clone URL.


2). Create a virtual environment. Using the command (virtualenv ~"name" ). And activate the Virtualenv.


3). Run the requirement package , using the command "pip install -r requirements.txt"


4). Run the migration steps. 'python manage.py makemigration' and 'python manage.py migrate'


5). Run the application in localhost(command: python manage.py runserver) or Public IP (command: python manage.py   runserver       0.0.0.0:PORT)



Example: http://127.0.0.1:8000/

Technologies :
Python 2.x, Django 1.11.3, pytz==2017.2


