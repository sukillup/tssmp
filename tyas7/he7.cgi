#!/usr/local/bin/python3.7
from wsgiref.handlers import CGIHandler
from hello7 import app
CGIHandler().run(app)