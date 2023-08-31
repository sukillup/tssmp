#!/usr/local/bin/python3.7 --
from wsgiref.handlers import CGIHandler
from helloM import app
CGIHandler().run(app)