from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np
from sklearn.naive_bayes import GaussianNB
import pandas as pd

# Load the pre-trained GaussianNB model
model = GaussianNB()
model = load('gaussian_nb_model.pkl')

# Percentage in Communication skills


def get_commu_skill(grade):
    if grade == 'C':
        return 0
    elif grade == 'B':
        return 1
    elif grade == 'A':
        return 2
# Hours working per day


def get_hour_working(hour_string):
    hour = int(hour_string)
    if hour < 4:
        return 4
    elif hour > 12:
        return 12
    else:
        return hour
# coding skills rating


def get_coding(coding_string):
    class_coding = {'Advanced Beginner': 0, 'Competent': 1,
                    'Proficient': 2, 'Novice': 3, 'Expert': 4}
    if coding_string in class_coding:
        return class_coding[coding_string]
    else:
        raise ValueError("Invalid experience level string")
# self-learning capability


def get_selflearn(selflearn_bool_string):
    if selflearn_bool_string.lower() == "yes":
        return 0
    elif selflearn_bool_string.lower() == "no":
        return 1
    else:
        raise ValueError("Input string must be 'yes' or 'no'")
# Interested subjects


def get_interest_subject(subject_string):
    subject = {
        'cloud computing': 0,
        'Computer Architecture': 1,
        'parallel computing': 2,
        'IOT': 3,
        'Software Engineering': 4,
        'hacking': 5,
        'data engineering': 6,
        'networks': 7,
        'programming': 8,
        'Management': 9
    }
    if subject_string in subject:
        return subject[subject_string]
    else:
        return None
# Taken inputs from seniors or elders


def get_input_senior(inputSenior_bool_string):
    if inputSenior_bool_string.lower() == "yes":
        return 1
    elif inputSenior_bool_string.lower() == "no":
        return 0
    else:
        raise ValueError("Input string must be 'yes' or 'no'")
# hard/smart worker


def get_worker(worker_bool_string):
    if worker_bool_string.lower() == "smart worker":
        return 1
    elif worker_bool_string.lower() == "hard worker":
        return 0
    else:
        raise ValueError(
            "Input string must be 'smart worker' or 'hard worker'")
# worked in teams ever?


def get_teamwork(teamwork_bool_string):
    if teamwork_bool_string.lower() == "yes":
        return 0
    elif teamwork_bool_string.lower() == "no":
        return 1
    else:
        raise ValueError("Input string must be 'yes' or 'no'")
# Suggest job role


def get_suggest_job(job_code):
    job_roles = {
        0: 'Database and Data Management',
        1: 'Project Management and Business Analysis',
        2: 'Software Dev and QA',
        3: 'Network Security and IT',
        4: 'Technical Support and System Analysis'
    }
    return job_roles.get(job_code, 'Error not correct index in jobs role')

# Make prediction function


def make_prediction_import(grade, hour_string, coding_string, selflearn_bool_string, subject_string, inputSenior_bool_string, worker_bool_string, teamwork_bool_string, model):
    # create a list of the attribute values
    grade = get_commu_skill(grade)
    hour_string = get_hour_working(hour_string)
    coding_string = get_coding(coding_string)
    selflearn_bool_string = get_selflearn(selflearn_bool_string)
    subject_string = get_interest_subject(subject_string)
    inputSenior_bool_string = get_input_senior(inputSenior_bool_string)
    worker_bool_string = get_worker(worker_bool_string)
    teamwork_bool_string = get_teamwork(teamwork_bool_string)
    # create a list of the attribute values
    attribute_values = [grade, hour_string, coding_string, selflearn_bool_string,
                        subject_string, inputSenior_bool_string, worker_bool_string, teamwork_bool_string]

    # create a new row of data for the 8 attribute values
    attr = ['Percentage in Communication skills', 'Hours working per day', 'coding skills rating', 'self-learning capability?',
            'Interested subjects', 'Taken inputs from seniors or elders', 'hard/smart worker', 'worked in teams ever?']
    attr_dict = {attr[i]: attribute_values[i] for i in range(len(attr))}
    test_data = pd.DataFrame([attr_dict])

    # use the model to predict the target variable for the new row of data
    # extract the integer value from the array
    y_pred = model.predict(test_data)[0]
    result = get_suggest_job(y_pred)
    return result


# Create a Flask app
app = Flask(__name__, template_folder="templates", static_folder='static')

# Define a route to handle GET requests to the root URL


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input.html', methods=['GET'])
def get_input():
    return render_template('input.html')
# Define a route to handle POST requests to the '/predict' URL


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Get the attribute values from the form
    attribute_values = [request.form['grade'], request.form['hour_string'], request.form['coding_string'], request.form['selflearn_bool_string'],
                        request.form['subject_string'], request.form['inputSenior_bool_string'], request.form['worker_bool_string'], request.form['teamwork_bool_string']]
    # Use the pre-trained model to make a prediction
    prediction = make_prediction_import(*attribute_values, model)
    response = {'prediction': prediction}
    # return jsonify(response)
    # # Render the prediction result on a new page
    return render_template('ITcareer.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
