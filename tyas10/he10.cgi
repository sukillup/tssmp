#!/usr/local/bin/python3.7
from wsgiref.handlers import CGIHandler
from hello10 import app
CGIHandler().run(app)