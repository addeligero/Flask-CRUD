from flask import render_template, request
from models import Person

def register_routes(app, db):
    @app.route('/')
    def index():
        people = Person.query.all()
        return '<br>'.join(f"{p.first_name} {p.last_name} - {p.age}" for p in people)
  
