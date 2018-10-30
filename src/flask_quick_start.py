from flask import Flask
app = Flask(__name__)

"""
# to build the server
export FLASK_APP=hello.py
python -m flask run
#python -m flask run --host=0.0.0.0 for public use over network
"""

@app.route('/')
def hello_world():
    return 'Hello'


