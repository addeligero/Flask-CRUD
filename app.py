from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/hi')
def hello():
    return "Hello from the hello function!"


@app.route('/handle_params')
def handle_params():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"Hello {name}, you are: {age}"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)