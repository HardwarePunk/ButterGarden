#!/bin/bash

# Initialize the database using init_db.py
python init_db.py

# Start gunicorn
exec gunicorn -c gunicorn.conf.py app:app
