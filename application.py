import os
import re
from flask import Flask, jsonify, render_template, request
import sys


# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")