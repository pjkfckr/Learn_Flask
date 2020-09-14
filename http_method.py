from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': # method가 POST일때 return "Login"
        return "Login"
    else:
        return "Show Login"


if __name__ == '__main__':
    app.run(debug=True)


"""
HTTP Method는 클라이언트가 서버에 요청된 페이지를 통해서 무엇을 하도록 원하는지 말해준다.

GET = 브라우저가 어떤 페이지에 저장된 정보만을 얻기 위해 서버에 요청하고서버는 그 정보를 보낸다. 가장 일반적인 method이다.

HEAD = 브라우저가 어떤 페이지에 저장된 내용이 아니라 헤더에 불리는 정보를 요청한다.
       어떤 Application이 GET 요청을 받은것 처럼 처리하나, 실제 내용이 전달되지 않는다.
       하부에 있는 Werkzeug 라이브러리들이 그런 처리를 하기 때문에 flask에서 처리 할 필요가 없다.

POST = 브라우저는 서버에게 새로운 정보를 "전송" 하도록 특정 URL에 요청하고 그 정보가 오직 한번 저장되는것을 보장하도록한다.
       이것이 보통 HTML Form을 통해서 서버에 데이터 전송하는 방식이다.

PUT = POST와 유사하지만 서버가 오래된 값들을 한번 이상 덮어쓰면서 sotre procedure를 여러번 실행할 수 있다.
      왜 유용할까? 에 대한 몇가지 이유가 있다.
      전종시 연결을 잃어버리는 경우를 생각해보면, 브라우저와 서버사이에서 정보의 단절없이 요청을 다시 안전하게 받을 수도 있다.
      POST는 단 한번 요청을 제공하기 때문에 이런 방식은 불가능하다.

DELETE = 주어진 위치에 있는 정보를 제거한다.

OPTIONS = 클라이언트에게 요청하는 URL이 어떤 method를 지원하는지 알려준다.
"""
