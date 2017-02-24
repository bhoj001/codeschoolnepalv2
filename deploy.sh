#!/usr/bin/env bash
# activate the virtual env
source venv/bin/activate
# migrate the database
cd src
python manage.py makemigrations
python manag.py migrate
# run the collect static command
python manage.py collectstatic
# export the environment variables
source src/.env
