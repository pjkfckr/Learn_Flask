"""
동적인 웹 어플리케이션은 정적 파일을 필요로 한다. 보통 JS나 CSS파일을 의미한다.
이상적으로 웹서버는 정적 파일들을 서비스하지만, 개발시에는 flask가 그 역활을 대신해준다.
"static"이라는 폴더를 생성한 package아래에 만들거나 module옆에 위치시키면,
개발된 application에서 /static 위치에서 정적 파일을 제공할 것이다.
"""
# 정적파일에 대한 URL을 얻으러면, 특별한 "static" 끝점 이름을 사용해야 한다.
# url_for('static', filename='style.css')
# 이 파일(style.css)는 파일시스템에 static/style.css로 저장되어야 한다.

