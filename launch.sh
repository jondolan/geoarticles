#!/bin/bash

export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
python3 -m flask run
