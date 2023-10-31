# -*- encoding: utf-8 -*-
"""
Python_Assignment
"""

from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    url_prefix=''
)
