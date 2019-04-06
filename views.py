from flask import Flask, request, abort, Blueprint

from flask_restplus import Resource, fields, Api
import datetime
import requests
from requests.auth import HTTPBasicAuth
import jwt
from utils import print_something

api_blueprint = Blueprint('api', __name__)
api_docs = Api(api_blueprint, doc="/")

api = api_docs.namespace('api', description='Backend main API')

@api.route('/test')
class Example(Resource):
	def get(self):
		x = print_something("hello")
		return {"hello":x}
