from flask import Flask
import json

app = Flask(__name__)

data = """{
"course": 411,
"courseName": "Software in Telecommunications",
"releaseYear": 2021,
"courseActive": true,
"droppedStudents": null,
"date": 08102021,
"someData": [[11,2], [22, 4], [33, 1], [44,5]],
"scores": {"a":77, "b":46, "c":91}
}"""

json_data = json.loads(data)

@app.route('/', methods = ['GET'])
def hello_world():
    return 'hello world!'

@app.route('/data', methods = ['GET'])
def send_data():
    return json_data

@app.route('/scores', methods = ['GET'])
def scores():
    return json_data["scores"]

@app.route('/scores/<score_value>', methods = ['GET'])
def score_value(score_value):
    if score_value in ['a', 'b', 'c']:
        return str(json_data["scores"][score_value])
    else:
        return "No data " + score_value + " !  Try with a, b or c !"

if __name__ == '__main__':
    app.run()

