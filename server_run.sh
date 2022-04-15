#!/bin/bash
# This script must contain a series of commands to run the backend application
# Eg:- For Node.js project;
#       npm run start
# Eg:- For SpringBoot Project;
#       ./gradlew bootRun
# Eg:- For Python Flask Project
#       export FLASK_APP=main.py
#       flask run
python ./Xharktank/manage.py migrate
python ./Xharktank/manage.py runserver 8081
