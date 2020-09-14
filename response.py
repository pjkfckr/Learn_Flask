# coding=utf-8
"""
View 함수로부터 반환되는 값은 자동으로 response 객체로 변환된다.
만약 return 값이 문자열이라면 response body로
"200 ok", "text/html" mimtype을 갖는 response객체로 변환된다.
Flask에서 반환값을 response 객체로 변환하는 로직
"""
# 1. 만약 정확한 유형의 response 객체가 반환된다면 그 객체는 그대로 view로 부터 반환되어 진다.
# 2. 만약 문자열이 반환된다면, reponse객체는 해당 data와 기본 parameter들을 갖는 response객체가 생성된다.
# 3. 만약 tuple 이 return 된다면 tuple 안에 있는 item들이 추가적인 정보를 제공할 수 있다.
#    tuple들은 지정된 form(response, status, headers) 이여야 하며 그 중 하나의 item이 tuple 이어야 한다.
#    status 값은 status code를 override 하면 'headers'는 추가적인 정보의의 list, dictionary가 될 수 있다.
# 4. 만약 위에 로직이 안된다면, Flask는 반환값이 유효한 WSGI application 이라고 가정하고
#    WSGI application을 response객체로 변환할 것이다.

# view에서 response 객체를 찾기 원한다면 make_response() 함수를 사용할 수 있다.

@app.errorhnadler(404)
def not_found(error):
    return render_template('error_.html'), 404

# make_response() 함수를 사용하여 반환되는 표현을 래핑하고, 변경을 위해 결과 객체를 얻은 다음 반환하면 된다.

@app.errorhnadler(404)
def not_found(error):
    response = make_response(render_template('error.html'), 404)
    response.headers['X-Something'] = 'A value'
    return response