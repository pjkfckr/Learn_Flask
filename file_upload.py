"""
Flask를 사용하여 쉽게 업로드된 파일들을 다룰 수 있다. 
HTML form에 "enctype='multipart/form-data'" 를 설정하면 된다.
그렇지 않으면 brower는 파일을 전혀 전송하지 않을 것이다.
"""

"""
업로드된 파일들은 메모리나 파일시스템의 임시 장소에 저장된다. "files" 객체의 files 속성을 찾아
그 파일들에 접근할 수 있다.
업로드된 파일들은 그 dictionary 안에 저장되어 있다.
서버의 파일시스템에 파일을 저장하도록 하는 "save()" method 또한 가지고 있다.
"""

from flask import request
from werkzeug import secure_filename


@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if reqeust.method == 'POST':
        f = reqeust.files['the_file']
        f.save('/uploads/uploaded_file.txt')

"""
application에 파일이 업로드 되기 전에 클라이언트에서의 파일명을 알고싶다면,
"filename" 속성에 접근할 수 있다.
하지만, 이 값은 위조될 수 있으며 결코 신뢰할 수 없는 값이다.
만약 서버에 저장되는 파일명을 클라이언트에서의 파일명을 그대로 사용하기 원한다면, Werkzeug에서 제공하는
"secure_filename()" 함수에 그 파일명을 전달하면 된다.
"""

@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if reqeust.method == 'POST':
        f = request.files['the_file']
        f.save('/uploads/' + secure_filename(f.filename))





