# django_todo_app

python django를 활용한 웹 개발 todo 게시판 만들기

3가지 폴더

- todoSubject
    - MySQL 데이터 베이스를 활용한 todo list 개발
    - todo_main : main 화면 app
    - todo_board : todo list를 작성하는 화면

- todoSubject_use_restfulAPI
    - restful api를 활용한 todo list 개발
    - todo_main : main 화면 app
    - todo_board : todo list를 작성하는 화면

- todoSubject_restfulAPI
    - restful api 서버


**!! restful api는 느리기에 DB 버전 사용 권장 !!**

# 개발 환경

- server
    - centos 7  (윈도우에서도 사용 가능 -> 단, localhost로 사용 가능)

- db
    - MySQL

- python
    - 3.6 ver
    - Django2.1.2
    - djangorestframework
    - requests etc

- javascript
    - sortable.js
    - jquery-3.2.1.min.js

- css
    - bootstrap 3.4.0

# 설치

리눅스 서버 설치 과정
- python3 설치 및 환경 설정
- python3 가상환경 생성(위와 동일한 폴더명)
  - 가상 환경에서 아래와 같은 라이브러리 설치
  - pip install django==2.1.2 pandas numpy pymysql requests uwsgi
- python3 manage.py makemigraions, python3 manage.py migrate 수행
- nginx, uwsgi 환경 연동 혹은 runserver 기능으로도 사용 가능


**다운받은 파일 실행 방법**

(데이터베이스 이용)
1. todoSubject -> python manage.py runserver 127.0.0.1:8088
    -> http://localhost:8088/board/

(restful apoi 이용)
1. todoSubject_restfulAPI -> python manage.py runserver 127.0.0.1:8000
2. todoSubject_use_restfulAPI -> python manage.py runserver 127.0.0.1:8080
    -> http://localhost:8080/board/


# restful API

- /todo_list/
    - 전체 리스트 출력

- /todo_list/create/
    - 데이터 추가

- /todo_list/1/
    - 숫자에 따른 detail 출력

- /todo_list/1/update/
    - 숫자에 따른 update

- /todo_list/1/delete/
    - 숫자에 따른 delete

