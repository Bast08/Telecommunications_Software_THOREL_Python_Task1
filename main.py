from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.config["DEBUG"] = True

data = """{
"course": 411,
"courseName": "Software in Telecommunications",
"releaseYear": 2021,
"courseActive": true,
"droppedStudents": null,
"date": 20211008,
"someData": [[11,2], [22, 4], [33, 1], [44,5]],
"scores": {"a":77, "b":46, "c":91}
}"""

scores_index = ['a', 'b', 'c']

json_data = json.loads(data)

@app.route('/', methods = ['GET'])
def hello_world():
    return 'hello world'

@app.route('/data', methods = ['GET'])
def send_data():
    return json_data

@app.route('/scores', methods = ['GET',  'POST', 'DELETE'])
def scores():
    if request.method == "GET":
        return json_data["scores"]
    elif request.method == "POST":
        posted_data = request.form.get('a')
        return posted_data
    else:
        json_data["scores"].clear()
        return "data deleted ! Use the GET method to verify."

@app.route('/scores/<score_value>', methods = ['GET', 'PATCH', 'PUT'])
def score_value(score_value):

    if request.method == "GET":
        if score_value in scores_index:
            return str(json_data["scores"][score_value])
        else:
            return "No data " + score_value + " !  Try with a, b or c ! If you want you can add the data " + score_value + " by using the PUT method."

    elif request.method == "PATCH":
        if score_value in scores_index:
            patched_value = request.form.get(score_value)
            if patched_value == '' or patched_value is None:
                return 'error, use a form where the keys is "' + score_value + '" and the value is an int.'
            else:
                json_data["scores"][score_value] = int(patched_value)
            return 'The data ' + score_value + 'is patched ! Visit /scores to verify.'
        else:
            return 'The data ' + score_value + ' need to be added before being patched ! Use the PUT method to add a new data.'
    else:
        added_value = request.form.get(score_value)
        if added_value == '' or added_value is None:
            return 'error, use a form where the keys is "' + score_value + '" and the value is an int.'
        else:
            scores_index.extend(score_value)
            json_data["scores"][score_value] = int(added_value)
            return "Data " + score_value + " added ! Visit /scores to verify"


if __name__ == '__main__':
    app.run()
