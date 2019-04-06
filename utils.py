from flask import Flask, request, abort, Blueprint

from flask_restplus import Resource, fields, Api
import datetime
import requests
from requests.auth import HTTPBasicAuth
import jwt

def print_something(smg):
	print(smg)
	return "from utils.py"
