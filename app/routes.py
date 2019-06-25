from flask import render_template
from app.forms import LoginForm
from app import app

@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Brian'}
    posts = [
        {
            'author': {'username': 'Sarah'},
            'body': 'Beautiful'
        },
        {
            'author': {'username': 'Joelle'},
            'body': 'Design Guru'
        }
    ]
    return render_template('home.html', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
