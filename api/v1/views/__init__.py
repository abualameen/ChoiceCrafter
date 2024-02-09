#!/usr/bin/python3
"""
the API Blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.criterias import *
from api.v1.views.results import *
from api.v1.views.alternatives import *
