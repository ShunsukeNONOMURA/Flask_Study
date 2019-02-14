#!/usr/bin/python3
# coding:UTF-8
""" app/controllers/auth_controller.py """
"""
直接POSTを受けるところを書く部分
これ自体がAPPにblueprint経由で呼ばれて、
これ自体が下記のモジュールを操作する。
"""

from flask import Blueprint, render_template
from app.models.modelA import modelA
mA = modelA()

# Blueprint
mod_moduleA = Blueprint('moduleA', __name__, url_prefix='/moduleA')

@mod_moduleA.route('/', methods=['GET'])
def index():
    return mA.print_val()
