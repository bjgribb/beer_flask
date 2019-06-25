from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)
