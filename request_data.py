"""
Web Application 에 있어서 Client에서 Server로 보내는 Data를 처리하는 것은 중요한 일이다.
Flask에서 이 정보는 글로벌한 "request" 객체에 의해 제공된다.
"""

"""
Context Local
Flask 에서 어떠한 객체들은 보통 객체들이 아닌 global 객체들이다.
이 객체들은 실제로 어떤 특정한 문맥에서 지역적인 객체들이 대한 대리자들이다.

Thread를 다루는 문맥을 생각해보면 된다.
웹에서 요청이 하나 들어오면, 웹서버는 새로운 thread를 하나 생성한다.
Flask가 내부적으로 요청을 처리할때, Flask는 현재 처리되는 thread를 활성화된 문맥이라고 간주하고,
현재 실행되는 application과 WSGI환경을 그 문맥(thread)에 연결한다.
이렇게 처리하는 것이 문맥을 지능적으로 처리하는 방식이고, application이 끊어짐없이
다른 application을 호출할 수 있다.
"""

"""
기본적으로 유닛 테스트 같은 것을 하지않는다면, 환전히 무시할 수 있다.
요청 객체에 의존하는 코드가 갑자기 깨지는것을 알게 될것인데, 왜냐하면 요청 객체가 존재하지 않기 때문이다.
해결책은 요청 객체를 생성해서 그 객체를 문맥에 연결하는 것이다.
유닛 테스트에 있어서 가장 쉬운 해결책은 "test_request_context()" 를 사용하는 것이다.
"with" 절과 함께 사용해서 test_request_context() 는 테스트 요청을 연결할 것이고,
그렇게 해서 그 객체와 상호 작용할 수 있다.
"""

from flask import request

with app.test_request_context('/hello', method='POST'):
    # 이제 assert 과 같이 with블록이 끝날 때 까지 요청으로 작업을 할수있다.
    # '/hello' 라는 경로를 지정한다.
    assert reqeust.path == '/hello'
    # 요청 method를 비교한다.
    assert request.method == 'POST'


# 또 다른 방법으론 WSGI 환경 변수를 "request_context()" method에 인자로 넘기는 것이다.
with app.reqeust_context(environ):
    assert reqeust.method == 'POST'


# Reqeust Object(요청 객체)
"""
현재 요청 method는 method 속성으로 사용할 수 있다. 
form data(HTTP POST 나 PUT 요청으로 전달된 데이터) 에 접근하려면
form 속성을 사용할 수 있다.
"""

@app.route('/login', method=['GET', 'POST'])
def login():
    error = None
    if reqeust.method == 'POST':
        # 유효한 로그인 form인지 확인
        if valid_login(reqeust.form['username'],
                       reqeust.form['password']):
            return log_the_user_in(reqeust.form['username'])
        
        else:
            error = 'Invalid username/password'
    # reqeust method 가 'GET' 이거나, 인증정보가 잘못됐을때 실행
    return render_template('login.html', error=error)

"""
위에 form에 접근한 키(username 이나 password)가 존재하지 않으면 KeyError가 발생한다.
"KeyError"로 예외처리를 할 수 있지만, 그렇지않는다면 HTTP 400(Bad Reqeust)에 대한
오류 페이지를 보여준다.
"""

# URL로 넘겨진 parameter 에 접근하려면, "args" 속성을 사용할 수 있다.
searchword = reqeust.args.get('key', '')

"""
args 속성의 get을 사용하거나 KeyError 예외처리를 하여 URL Parameter에 접근하는것이 좋다.
사용자가 URL을 변경할 수 있으며, 사용자에게 친근하지 않은 "Bad reqeust"를 보여주기 때문이다.
"""

