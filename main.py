from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/scores')
def scores():
    return 'this is where i will interact with scores data'

@app.route('/scores/<score_value>')
def score_value(score_value):
    return 'this is where i will interact with the value : ' + score_value

if __name__ == '__main__':
    app.run()
