from flask import Blueprint, request, Response, jsonify, url_for,\
    redirect, render_template, render_template_string, session


login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login')
def login():
    login_page = '''
    <form action="{{ url_for('login_bp.do_login') }}" method="post">
        <p>name: <input type="text" name="user_name" /></p>
        <input type="submit" value="Submit" />
    </form>
    '''
    return render_template_string(login_page)


@login_bp.route('/do_login', methods=['POST'])
def do_login():
    name = request.form.get('user_name')
    session['user_name'] = name
    user_info = {
        'name': name,
        'email': '123@aa.com',
        'age': 0
    }
    return render_template('user_info.html', page_title='CCB Home', user_info=user_info)


@login_bp.route('/logout')
def logout():
    # session.get('user_name')
    session.pop('user_name', None)
    return redirect(url_for('login_bp.login'))


@login_bp.route('/register')
def register():
    return render_template('register.html')


@login_bp.route('/do_register', methods=['POST'])
def do_register():
    # print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    # 取 name=letian&password=123 这种用过&符号分割的key-value键值对格式
    # print(request.form.getlist('name'))
    # print(request.form.get('name', default='little apple'))

    name = request.form.get('name')
    password = request.form.get('password')

    # POST的数据是JSON格式，request.json会自动将json数据转换成Python类型（字典或者列表）
    # 注意，postman 请求头中Content-Type的值是application/json。
    # print(type(request.json))
    # name = request.json['name']
    # name = request.json['password']

    return redirect(url_for('login_bp.login'))
