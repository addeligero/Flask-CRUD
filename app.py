from flask import Flask,request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    
    
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/welcome')
def hello():
    return render_template('index.html')


@app.route('/handle_params')
def handle_params():
    if 'name' in request.args.keys() and 'age' in request.args:
        name = request.args.get('name')
        age = request.args.get('age')
        return f"Hello {name}, you are: {age}"
    
    else:
        return "Please provide both 'name' and 'age' parameters in the query string."

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)