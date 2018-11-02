from __future__ import print_function
from flask import Flask, url_for, render_template, request
import json
app = Flask(__name__)

"""
# to build the server
export FLASK_APP=hello.py
python -m flask run
#python -m flask run --host=0.0.0.0 for public use over network
"""

@app.route("/")
def index():
    # hello world of flask
    return "Hello World"

@app.route("/projects/")
def projects():
    # Cononical url for folder structure includes a trailing slash
    return "Projects"

@app.route("/experiment/<string:id>")  # <uuid:id>
def show_post(id):
    # Show the post with the given id, the id is an integer
    return "Post {}".format(id)

@app.route("/simple_template")
def template():
    # Using render templates
    # templates will be folder that is a package (if app is a package)
    # or will be a module if app is a module
    return render_template('hello.html', name="Hello World!")

@app.route("/show_surface", methods=["GET", "POST"])
def show_surface():
    fname = "tmp_ram_flask.json"
    if request.method == 'POST':
        data = request.get_json()
        print(json.dumps(data, indent=4))

        # Make a temporary json file
        with open(fname, 'w') as json_file:
            json.dump(data, json_file)
        return "post - {}".format(type(data))

    else:
        # Load the temporary json file
        with open(fname, 'r') as json_file:
            data = json.load(json_file)
        str_data = json.dumps(data, indent=4)
        print(str_data)
        return "get - {}".format(str_data)

# tell Flask to behave as though handling a rerquest enve while
# we use Python shell
# use url_for method, which is pythonic way to generate urls
with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_post', id='JohnDoe'))
    print(url_for('static', filename='style.css')) # serving static files in /static folder

app.run(debug = True)