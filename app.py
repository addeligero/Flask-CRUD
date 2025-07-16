from flask import Flask

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

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)