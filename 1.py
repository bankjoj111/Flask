from flask import Flask

app = Flask(__name__)

@app.route('/<opt>/<int:a>/<int:b>')
def calculate(opt, a, b):
    if opt == 'add':
        ans = a + b
    elif opt == 'sub':
        ans = a - b
    elif opt == 'mul':
        ans = a * b
    elif opt == 'div':
        if b == 0:
            return '<h3>Error: Division by zero is not allowed</h3>', 400
        ans = a / b
    else:
        return '<h3>Error: Invalid operator</h3>', 400

    return f'<h3>{a} {opt} {b} = {ans}</h3>'

@app.route('/')
def index():
    return 'Lab 9_4 - Calculator'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port='5000')
