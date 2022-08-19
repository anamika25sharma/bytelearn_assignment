from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    date = datetime.now()
    return "Hello world!"


@app.route('/time')
def time():
    date = datetime.now()
    return str(date)

if __name__=='__main__':
    ps = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=ps)
