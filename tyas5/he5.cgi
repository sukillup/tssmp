#!/usr/local/bin/python3.7
from wsgiref.handlers import CGIHandler
from hello5 import app
CGIHandler().run(app)