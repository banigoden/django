#!/bin/bash

#Apply database migrations
python manage.py migrate

# Load initial data from the backup file
psql -U web_user -h postgres -p 5432 -d denisbandurin -f /docker-entrypoint-initdb.d/backup_file.sql


python manage.py runserver 0.0.0.0:8000