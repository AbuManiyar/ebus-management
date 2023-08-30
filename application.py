from flask import Flask,render_template
import logging
logging.basicConfig(filename='ebus.log', level=logging.DEBUG)


application =  Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

