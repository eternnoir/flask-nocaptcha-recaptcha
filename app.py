# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

SITE_KEY = '6LfX2v4SAAAAAE22aaDgFzgZazm10BlagFziVxk-'
SECRET_KEY = '6LfX2v4SAAAAAHSlw95qrK45Lp_pw0OSdHt7I7L5'

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello World!'
