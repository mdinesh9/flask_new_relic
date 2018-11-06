import sys

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


def infinite_function(n):
    print(infinite_function(n+1))

@app.route("/test")
def test_one():
    return render_template("test_one.html")

@app.route("/test2")
def test_two():
    return render_template("test_two.html")


@app.route("/test3")
def test_three():
    infinite_function(1)

@app.route("/test4")
def test_four():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)


    