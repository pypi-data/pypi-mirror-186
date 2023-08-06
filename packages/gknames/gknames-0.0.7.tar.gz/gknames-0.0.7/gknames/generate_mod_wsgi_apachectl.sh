#!/bin/bash
# Create a setup script and immediately start the apache instance.  Our URL prefix
# is specified by the --mount-point setting.  We need to specify a PYTHONPATH before
# starting the apache instance. Run this script from THIS directory.
# 
# REQUIREMENTS:
# Write a file in ~/.config/django/django_env_$CONDA_DEFAULT_ENV (e.g. panstarrs)
# The contents of this file should be as follows:
# export DJANGO_SECRET_KEY=''
# 
# export DJANGO_MYSQL_DBUSER=''
# export DJANGO_MYSQL_DBPASS=''
# export DJANGO_MYSQL_DBNAME=''
# export DJANGO_MYSQL_DBHOST=''
# export DJANGO_MYSQL_DBPORT=''
# 
# export WSGI_PORT=''
# export WSGI_PREFIX=''
#
# Specifiy what to add as the name prefix
# export DJANGO_OBJECT_PREFIX='PS'
# OR
# export DJANGO_OBJECT_PREFIX='ATLAS'
#
# Specify which naming scheme to use. Pan-STARRS uses 1=a
# and single letters eventually become double, triple, etc
# but ATLAS uses 1 = aab with leading base26 zeros (a).
# export DJANGO_OBJECT_NAMING_SCHEME='a'
# OR
# export DJANGO_OBJECT_NAMING_SCHEME='aab'


if [ -f ~/.config/django/django_env_$CONDA_DEFAULT_ENV ]; then chmod 600 ~/.config/django/django_env_$CONDA_DEFAULT_ENV; source ~/.config/django/django_env_$CONDA_DEFAULT_ENV; fi

export APACHEPATH="/tmp/nameserver"

if [ $DJANGO_MYSQL_DBNAME ]
then
    export APACHEPATH=/tmp/$DJANGO_MYSQL_DBNAME
fi

export PORT=8085
if [ $WSGI_PORT ]
then
    export PORT=$WSGI_PORT
fi

export PREFIX=/nameserver
if [ $WSGI_PREFIX ]
then
    export PREFIX=$WSGI_PREFIX
fi

if [ -f $APACHEPATH/apachectl ]; then
    echo "Stopping Apache if already running"
    $APACHEPATH/apachectl stop
    sleep 1
    # wait a second to make sure the port is released
else
    echo "Creating directory $APACHEPATH"
    mkdir -p APACHEPATH
fi

mod_wsgi-express setup-server --working-directory nameserver --url-alias $PREFIX/static static --url-alias $PREFIX/media media --application-type module nameserver.wsgi --server-root $APACHEPATH --port $PORT --mount-point $PREFIX


export PYTHONPATH=$(pwd)
$APACHEPATH/apachectl start
