#!/bin/sh
echo "Hello, let's start the API!"
export FLASK_APP=index.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export CONFIG=Local
flask run
