# coding=utf-8

# Request object 외에도 하나의 요청에서 다음 요청까지 사용자에 대한 구체적인 정보를
# 저장할 수 있는 'session' 이라는 객체가 있다.
# 세션은 쿠키에서 구현되어 지고 암호화를 사용하여 그 쿠키를 서명한다.
# 사용자는 쿠키의 내용을 볼 수는 있지만, 서명을 위해 사용된 비밀키를 알지 못한다면
# 쿠키의 내용을 변경할 수 없다는 것을 의미한다.

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action='' method='post'>
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret Key. Keep this really secret
app.secret_key = ''
# OS를 import 하여 비밀키를 무작위로 생성할수있다.
# import os
# os.urandom(24)
# cryptographic random generator(암호 난수 발생기)

if __name__ == '__main__':
    app.run(debug=True)


