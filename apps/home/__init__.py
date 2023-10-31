# -*- encoding: utf-8 -*-
"""
Python_Assignment
"""

from flask import Blueprint

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)
