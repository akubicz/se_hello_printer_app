from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request
from flask import url_for, redirect

moje_imie = "Anna"
msg = "Hello World!"


@app.route("/")
def index():
    output = request.args.get("output")
    name = request.args.get("name")
    if not output:
        output = PLAIN
    if name is None:
        return get_formatted(msg, moje_imie, output.lower())
    else:
        return get_formatted(msg, name, output.lower())


@app.route("/outputs")
def supported_output():
    return ", ".join(SUPPORTED)


@app.route('/testhtml')
def testhtml():
    return redirect(url_for('static', filename='example.html'))
