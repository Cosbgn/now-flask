
from flask import Flask, redirect
from flask_restplus import Resource, Api, fields
from werkzeug.contrib.fixers import ProxyFix
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)



from views import api_blueprint
app.register_blueprint(api_blueprint)
