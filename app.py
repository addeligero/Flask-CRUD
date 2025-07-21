from flask import Flask,request, render_template, request,session

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key='SOME KEY'

@app.route('/', methods=['GET' ,'POST'])
def index():
     if request.method == 'GET':
        return render_template('index.html')
     else:  # Handles POST
        username = request.form.get('username')
        password = request.form.get('password')
        return f"Welcome {username}, your password is: {password}"

@app.route('/setting_session')
def setting_session():
    session['name']='Adrian'
    session['age'] = 30  
    return render_template('setting_session.html')

@app.route('/set')
def set():
    name=session['name']
    age=session['age']   
    message = f"Session set with name: {name} and age: {age}"
    return render_template('setting_session.html', message=message)


# This route handle parameters from the query string
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