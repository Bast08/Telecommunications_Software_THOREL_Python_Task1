from flask import Flask
import json
app = Flask(__name__)

data = """{
"course": 411,
"courseName": "Software in Telecommunications",
"releaseYear": 2021,
"courseActive": true,
"droppedStudents": null,
"date": 20210218,
"someData": [[11,2], [22, 4], [33, 1], [44,5]],
"scores": {"a":77, "b":46, "c":91}
}"""

json_data = json.loads(data)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/data')
def send_data():
    return json_data

@app.route('/scores')
def scores():
    return json_data["scores"]

@app.route('/scores/<score_value>')
def score_value(score_value):
    return 'this is where i will interact with the value : ' + score_value

if __name__ == '__main__':
    app.run()
