#!/bin/bash

NAME="DjangoBlog"
DJANGODIR=/root/ENV/python3/DjangoBlog
# SOCKFILE=/root/ENV/python3/run/gunicorn.sock
USER=root # the user to run as
GROUP=root # the group to run as
NUM_WORKERS=2 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=DjangoBlog.settings # which settings file should Django use
DJANGO_WSGI_MODULE=DjangoBlog.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /root/ENV/python3/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
# RUNDIR=$(dirname $SOCKFILE)
# test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn DjangoBlog.wsgi:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
