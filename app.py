from flask import Flask
from flask import request
import ast
from sklearn import svm
import numpy as np


app = Flask(__name__)

input_set = [[], []]
output_set = []

input_set = [[0, 0, 0, 0], [0, 0, 0, 0]]
output_set = [0, 0]
clf = svm.SVC(kernel='linear', C=1.0)


@app.route('/train')
def train():
    print(request.args.get('input'))
    print(request.args.get('output'))
    input_set.append(ast.literal_eval(request.args.get('input')))
    output_set.append(int(request.args.get('output')))
    clf.fit(np.array(input_set), output_set)
    writeToFile()
    return "trained new data"


@app.route('/predict')
def predict():
    try:
        return str(clf.predict(ast.literal_eval(request.args.get('data'))))
    except Exception as e:
        return str(e)


@app.route('/print')
def printData():
    return str(input_set) + str(output_set)

def writeToFile():
    print("Opening the file...")
    target = open("db.txt", 'w')
    for index in range(len(input_set)):
        for i in range(len(input_set[index]) - 1):
            target.write("%s," % input_set[index][i])
        target.write("%s\n" % input_set[len(input_set) - 1][len(input_set[index]) -1])
        target.write("%s\n" % output_set[index])


def readFromFile():
    print("Opening the file...")
    with open("db.txt", "r") as f:
        lines = f.readlines()
    for index in range(len(lines)):
        if(index % 2 == 0):
            input_set.append(lines[index].rstrip('\n').split(","))
        else:
            output_set.append(lines[index].rstrip('\n'))

if __name__ == '__main__':
    readFromFile()
    app.run(host='0.0.0.0', port='8804')