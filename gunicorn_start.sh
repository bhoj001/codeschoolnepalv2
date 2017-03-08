#!/bin/bash

# Name of an application
NAME="CodeSchoolNepal"
# project directory
PROJECTDIR=/webapps/codeschoolnepal.com
# django project virutalenv directory
VENVDIR=/webapps/codeschoolnepal.com/venv
# Project source directory
SRCDIR=/webapps/codeschoolnepal.com/master/src
# Sock file as gunicorn will communicate using unix socket
SOCKFILE=$PROJECTDIR/gunicorn.sock
# Name of the application
NAME="codeschoolnepal"
# User who runs the app
USER=webapps
# the group to run as
GROUP=webapps
# how many worker processes should Gunicorn spawn
NUM_WORKERS=3
# which settings file should Django use
DJANGO_SETTINGS_MODULE=codeschool.production_settings
# WSGI module name
DJANGO_WSGI_MODULE=codeschool.wsgi

# Activate the virtual environment
source $VENVDIR/bin/activate
# Export the settings module
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# move to src dir
cd $SRCDIR
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $VENVDIR/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
