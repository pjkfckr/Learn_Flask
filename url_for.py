from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '%s Profile' % username


# test_request_context 를 쓰는 이유
"""
1. URL 역변환이 URL을 하드코딩하는것 보다 훨씬 설명적이다.
    이 방식은 전체적으로 URL 이 어디있는지 기억할 필요없이 한번에 URL을 다 변경할 수 있다.

2. URL을 얻어내는 것은 특수 문자 및 유니코드 데이타에 대한 이스케이핑을 명확하게 해주기 때문에 처리할 필요가 없다.

3. 작성한 Application이 URL의 최상위 바깥에 위치한다면, (EX) "/" 대신에 /myapplication)
    "url_for()가 그 위치를 상대적 위치로 적절하게 처리해줄것이다.
"""
with app.test_request_context(): 
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Park'))


if __name__ == '__main__':
    app.run(debug=True)