# coding=utf-8
# 쿠키
"""
쿠키에 접근하기 위해서는 "cookies" 속성을 사용할 수 있다.
쿠키를 저장하기 위해서는 response 객체의 "set_cookie" method를 사용할 수 있다.
request 객체의 "cookies" 속성은 Client가 전송하는 모든 cookie를 가지고 있는 dictionary 이다.
세션을 사용하기를 원한다면 쿠키를 직접 사용하는 대신에 쿠키에서 보안성을 추가한 flask의 세션을 사용하면 된다.
"""

# Reading cookies
from flask import request, make_response

@app.route('/')
def index():
    username = request.cookies.get('username')
    # cookierk 없는 경우 KeyError가 발생하지 않도록
    # cookies[key] 대신 cookies.get(key)를 사용


# Storing cookies
@app.route('/')
def index():
    response = make_response(render_template(...))
    response.set_cookies('username', 'the username')
    return response

"""
쿠키가 response 객체에 저장되는 것을 보면, 보통 view 함수로부터 String을 반환하기 때문에
Flask는 그 문자열들을 response 객체로 변환할 것이다. 만약 명시적으로 변환하기를 원한다면
"make_response()" 함수를 사용하여 값을 변경할 수 있다.
때때로 response 객체가 아직 존재하지 않는 시점에서 쿠키를 저장하기를 원할 수도 있다.
deferred(지연된) 요청 콜백 패턴을 사용하면 가능하다.
"""



