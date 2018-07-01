#!/bin/bash

export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
export MONGODB_CONNECTION_STRING=mongodb://localhost:27017/
python3 -m flask run
