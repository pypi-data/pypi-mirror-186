#coding:utf8
from functools import wraps
from flask import current_app
from .util import jsonres
from .Uiadmin import Uiadmin
from .CoreController import CoreController

# @app.before_request
# def basic_authentication():
#     if request.method.lower() == 'options':
#         return jsonres({});

