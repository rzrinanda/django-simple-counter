#django-counter-application
COUNTER USER BASED USING DJANGO

# django-counter-app
A simple counter application with django.

When the user presses a button, an integer displayed on the website increments by one. A user should only be allowed to press the button 5 times every 60 seconds. This means that if a user presses the button in the following order:

● 01:01:15 AM

● 01:01:20 AM

● 01:01:54 AM

● 01:01:59 AM

● 01:02:10 AM

They cannot press the button until 01:02:15 AM. If they press the button at 01:02:15AM they cannot press the button until 01:01:20 AM, et cetera.
The integer that is displayed on the website is the total number of button presses across all users.

installation instructions:

using pyenv and poetry

*run instructions:*

pyenv activate [environment_name]

poetry install 

python manage.py createsuperuser #optional if you don't have superuser account

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

