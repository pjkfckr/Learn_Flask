# coding=utf-8
# Redirection 과 Error
"""
사용자가 다른 end point 로 redirect 하기 위해서는 "redirect()" 함수를 사용해야한다.
Error code 를 가지고 일찍 요청을 중단하기를 원한다면 "abort()" 함수를 사용해야한다.
"""

from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

# 위 코드는 사용자가 인덱스 페이지에서 접근할 수 없는 페이지로 redirect 되어질 것이지 때문에
# 다소 무의미한 예제일 수는 있으나 어떻게 작동한다는 것을 보여주고 있다.

# 에러페이지를 변경하기를 원한다면 "errorhandler()" 데코레이터를 사용할 수 있다.

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# "render_template()" 호출 뒤에 있는 404는
# status code가 404가 되어야한다는 것을 Flask에 명시하는 것이다.



