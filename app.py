# -*- coding: utf-8 -*-
import urllib2
from flask import Flask, render_template, url_for, request
import json
app = Flask(__name__)

# Change to your site key and secret key.
# Check https://www.google.com/recaptcha/intro/index.html
SITE_KEY = '6LfX2v4SAAAAAE22aaDg*********************'
SECRET_KEY = '6LfX2v4SAAAAAHSlw9*********************'

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ''
    showalert = False
    if request.method == 'POST':
        response = request.form.get('g-recaptcha-response')
        showalert = True
        if checkRecaptcha(response,SECRET_KEY):
            msg = 'You are human.'
        else:
            msg='You are bot.'
    return render_template('index.html',
                           siteKey=SITE_KEY,
                           alertMsg = msg,
                           showAlert = showalert)

def checkRecaptcha(response, secretkey):
    url = 'https://www.google.com/recaptcha/api/siteverify?'
    url = url + 'secret=' +secretkey
    url = url + '&response=' +response
    try:
        jsonobj = json.loads(urllib2.urlopen(url).read())
        if jsonobj['success']:
            return True
        else:
            return False
    except Exception as e:
        print e
        return False


if __name__ == '__main__':
    app.debug = True
    app.run()
