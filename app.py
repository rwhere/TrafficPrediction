# CS-499 | Hack-3
# @authors: Ryan Waer & Wai Phyo

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import ast
from sklearn import svm
import numpy as np


app = Flask(__name__)
CORS(app)

# Starting with empty data sets
input_set = []
output_set = []
clf = svm.SVC(kernel='rbf', C=100.0, gamma=0.001)


# Training URL
# Example => /train?input=[1,2,3,4]&output=3
# 1. add to data set in memory
# 2. retrain
# 3. store to file for next time
@app.route('/train')
def train():
    try:
        input_set.append(ast.literal_eval(request.args.get('input')))
        output_set.append(int(request.args.get('output')))
        write_to_file()
        if len(input_set) == len(output_set) and len(input_set) > 1:
            clf.fit(np.array(input_set), output_set)
            return "trained new data"
        else:
            return "not enough data for new data"
    except Exception as e:
        return str(e)

# Prediction
# Example => /predict?data=[1,2,3,4]
# 1. return predicted data
# 2. return error in exception
@app.route('/predict')
def predict():
    try:
        return str(clf.predict(ast.literal_eval(request.args.get('data')))[0])
    except Exception as e:
        return str(e)

# Printing both input and output data set
@app.route('/print')
def print_data():
    return str(input_set) + str(output_set)


def write_to_file():
    print("Opening the file...")
    target = open("db.txt", 'w')
    for index in range(len(input_set)):
        for i in range(len(input_set[index]) - 1):
            target.write("%s," % input_set[index][i])
        target.write("%s\n" % input_set[index][len(input_set[index]) - 1])
        target.write("%s\n" % output_set[index])


def read_from_file():
    print("Opening the file...")
    with open("db.txt", "r") as f:
        lines = f.readlines()
    for index in range(len(lines)):
        if(index % 2 == 0):
            input_set.append(lines[index].rstrip('\n').split(","))
        else:
            output_set.append(lines[index].rstrip('\n'))


# Beginning of app, read from file to add to add to data sets in memory
if __name__ == '__main__':
    read_from_file()
    app.run(host='0.0.0.0', port='8804')
