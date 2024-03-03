from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
# from . import views
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incurrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signUp', methods=['GET' , 'POST'])
def sing_up():
    data = request.form

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName') 
        passw1 = request.form.get('password1')
        passw2 = request.form.get('password2') 

        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email already exists.', category='error')
        else:
            if len(email) < 4:
                flash('Email is must be greater then 4 characters.' , category='error')
            elif len(firstName) < 2:
                flash('First Name is must be greater then 2 characters.' , category='error')
            elif passw1 != passw2:
                flash('Password don\'t match.' , category='error')
            elif len(passw1) < 7:
                flash('Password must be greater then 7 characters.' , category='error')
            else:
                new_user = User(email = email, first_name = firstName, password = generate_password_hash(passw1))
                db.session.add(new_user)
                db.session.commit()
                user = User.query.filter_by(email = email).first()
                login_user(user, remember=True)
                flash('Account created!' , category='success')
                return redirect(url_for('views.home'))
    

    print(data)
    return render_template("signUp.html" , user = current_user)