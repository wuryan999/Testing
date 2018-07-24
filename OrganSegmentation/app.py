import os, sys
import math
import random

from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for, render_template, json, flash, make_response, send_from_directory, jsonify
from parse import parse
import subprocess, shlex
import requests
import re
import numpy as np
import pandas as pd
import logging

from AI_core import ICH_classifyer

IMAGE_FOLDER = './img'
RESULT_FOLDER = 'annotation'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'dcm'])

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.secret_key = 'MC_RYAN'

logging.basicConfig(format='%(asctime)s %(message)s')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route('/')
def welcome():
    return redirect('hello')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
