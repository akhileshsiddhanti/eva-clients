"""
sudo pip3 install flask
sudo pip3 install werkzeug
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jeremy'


from flask import Flask, request, Response, jsonify, url_for,\
    redirect, render_template, abort, render_template_string

from route.ImageInfoAction import image_info_bp
from route.LoginAction import login_bp
from route.query_server import query_server

app = Flask("my web APP", static_folder="static", template_folder="templates")
#app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'

app.register_blueprint(image_info_bp, url_prefix='/images')
app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(query_server, url_prefix='/query')

@app.errorhandler(401)
def page_unauthorized(error):
    return render_template_string('<h1> Unauthorized </h1><h2>{{ error_info }}</h2>', error_info=error)


@app.route('/user/<username>')
def user(username):
    user_info = {
        'name': username,
        'email': '123@aa.com',
        'age': 0,
        'github': 'https://github.com/letiantian'
    }
    return render_template('user_info.html', page_title='letian\'s info', user_info=user_info)


@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'hello ' + username


@app.route('/page/<int:num>')
def page(num):
    print(num)
    print(type(num))
    return 'hello world'


@app.route('/test1')
def test1():
    print('this is test1')
    return redirect(url_for('test2'))  # redirect


@app.route('/test2')
def test2():
    return 'this is redirecting to /test2'


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80, debug=True)

