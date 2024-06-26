'''
Flask Application
'''
from flask import Flask, jsonify, request, abort
from models import Experience, Education, Skill
from helpers.education_api import *

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    # This method return us a JSON object representing the data associated with the ID passed as query parameter
    # It can be None or an integer. If None it returns empty json object.
    if request.method == 'GET':
        index = request.args.get("id")
        return handle_education_get_request(request, index)

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education/', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    # This method return us a JSON object representing the data associated with the ID passed as query parameter
    # It can be None or an integer. If None it returns empty json object.
    if request.method == 'GET':
        index = request.args.get("id")
        return handle_education_get_request(request, index)

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
