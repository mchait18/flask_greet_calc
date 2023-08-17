# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

def add_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def sub_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def mult_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def div_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<ops>')
def call_operation(ops):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATIONS[ops](a, b)
    # print (result)
    return str(result)
