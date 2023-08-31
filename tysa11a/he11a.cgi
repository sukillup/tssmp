#!/usr/local/bin/python3.7 --
from wsgiref.handlers import CGIHandler
from hello11a import app
CGIHandler().run(app)