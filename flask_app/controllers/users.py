from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/users')
def read():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/users/new')
def show_form():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    ## error when redirecting; need to input id number from data
    return redirect('/users/<id>')

@app.route('/users/<id>')
def show_user(id):
    data = {
        'id_num' : id
    }
    user_info = User.get_user_info(data)
    print(user_info)
    return render_template('read_one.html', info = user_info)

@app.route('/users/<id>/destroy')
def delete_user(id):
    data = {
        'id_num' : id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/users/<id>/edit')
def edit_user(id):
    data = {
        'id_num' : id
    }
    user_info = User.get_user_info(data)
    print(user_info)
    return render_template('edit.html', info = user_info)

@app.route('/users/<id>/update', methods = ['POST'])
def update_info(id):
    data = {
        'id_num' : id,
        'new_fname' : request.form['new_fname'],
        'new_lname' : request.form['new_lname'],
        'new_email' : request.form['new_email']
    }
    User.edit(data)
    ## need to redirect to single user page
    return redirect('/users')
