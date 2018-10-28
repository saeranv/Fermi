from flask import Flask
app = Flask(__name__)

"""
# to build the server
export FLASK_APP=hello.py
python -m flask run
#python -m flask run --host=0.0.0.0 for public use over network
"""

"""
Next steps for astrobot.0.0.3
#obj: run astro calcs w/i gh over flask server
# 1 minimal gh component pushes gh vars in json (HB obj/Rhino) to GET 
# 2 flask REST takes json and pushes to astro. Does calcs return json
# 3 json vized in gh
# 4 json vized on local server

# Sprint 1
- ironpython script to build a simple json of gh srfs (time = 45min)
- HTTP method script to push to flask   
"""

@app.route('/')
def hello_world():
    return 'Hello'


