from flask import Flask, render_template, redirect, url_for, request

import requests
from datetime import date

app = Flask (__name__)

@app.route('/')
def index():
  return render_template('index.html')







if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')