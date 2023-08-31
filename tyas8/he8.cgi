#!/usr/local/bin/python3.7
from wsgiref.handlers import CGIHandler
from hello8 import app
CGIHandler().run(app)