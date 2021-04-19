## Flask Web 









virtualenv 설치 및 가상환경 세팅

```cmd
pip install virtualenv

#버전 확인을 통해서 설치 확인
virtualenv --version 

#
virtualenv flask_web & cd flask_web 

가상환경 활성화
Scripts\activate

(flask_web) C:\apps\flask_web> 
```

#### flask library 설치

```cmd
pip install flask
```



필요한 라이브러 설치후 관리 (pip 명령어)

###### 설치한 라이브러리를 requirements.txt에 기록

```cmd
pip freeze > requirements.txt
```



requirements.tx 에 기록된 라이브러리 설치 

```cmd
pip install -r requirements.txt
```





서버를 띄우기 위해 다음과 같이 app.py를 생성후 다음과 같은 코드를 작성한다.

```python
from flask import Flask 


app = Flask(__name__)

app.debug = True


if __name__ == '__main__':
  app.run()
```





클라이언트가 http://localhost:5000/data 으로 GET방식으로 요청이 들어왔을때 "Hello World !" 문구를 리턴해 본다.

그러기 위해서 다음과 같은 코드를 추가한다.



```python
from flask import Flask 


.....


@app.route('/data', methods=['GET'])
def index():
  return "Hello World"

.....
```



render_template 메소드를 이용해서 index.html을 화면에 랜더링 해본다.

templates/index.html 을 생성후 다음과 같이 코드를 추가한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  {{data}}
  <h1>Hello World!!</h1>
</body>
</html>
```



app.py의 def index(): 을 수정한다.

```python
@app.route('/data', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("index.html", data="KIM")
```

render_template 은 첫번째 인자로 html파일 경로 , 두번째 인자로 전달할 데이터를 

jinja2 엔진 문법

**{{ ... }} : 변수나 표현식의 결과를 출력하는 구분자(delimeter)**

 **{% ... %} : if문이나 for문 같은 제어문을 할당하는 구분자(delimeter)**

**{# ... #} : 주석**

 **{%- ... %}, {%+ ... %}, {% ... -%} ... : 공백 제거 혹은 유지**

 **{% raw %} ... {% endraw %} : 이스케이프**



예)

```html
{% for <개별요소> in <리스트> %}
<실행코드>
{% endfor %} 
```



클라이언트가 http://localhost:5000 으로 GET방식으로 요청이 들어왔을때   index.html 랜더링 되도록 다음과 같은 코드를 추가한다.



```python
from flask import Flask , render_template


.....


@app.route('/', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("index.html", data="KIM")

.....
```





index.html 파일을 만든후 다음과 같이 코딩을 한다. 

그런데 페이지마다 공통으로 적용되는 부분은 따로 만들어서 extends 한다.

공통으로 적용되는 파일을 layouts.html 을 생성후 다음과 같이 코딩한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title>Flask_Web</title>
</head>
<body>
  {% include "includes/_navbar.html" %}
  <div class="container">
        <!-- Content here --> 
        {% block body %}
        {% endblock %} 
      </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
```



{% block body %}

 ...... 부분에 들어갈 콘텐츠를 만든다.       

 {% endblock %}  

navigation bar를 다시 include 한다.

includes/_navbar.html 을 생성 

```html
<nav class="navbar navbar-expand-lg navbar-light bg-warning">
  <a class="navbar-brand" href="/">Flask_Web</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
          <li class="nav-item active">
              <a class="nav-link" href="/">Home
                  <span class="sr-only">(current)</span>
              </a>
          </li>
          <li class="nav-item">
              <a class="nav-link" href="/about">About</a>
          </li>
          <li class="nav-item">
              <a class="nav-link" href="/articles">Articles</a>
          </li>
      </ul>
  </div>
</nav>
```



index.html  다음과 같이 코드를 생성한다.

```html
{% extends "layouts.html" %}
 
  {% block body %}
  <h1 class="display-4">HOME PAGE</h1>
<p class="lead">This Application is build using by python and Flask Framework</p>
<hr class="my-4">
<a class="btn btn-warning btn-lg" href="#" role="button">Learn more</a>
  {% endblock %}
  

```







{% block body %}

..... 생성   

  {% endblock %}



다음과 같은 페이자 완성 되었다.

![image-20210419145516756](https://user-images.githubusercontent.com/25717861/115188072-52ca9b80-a11f-11eb-9ff2-b067f8bc6d1b.png)



http://localhost:5000/about 페이지 구성을 위해서 app.py 에 다음과 같은 코드를 추가한다.

```python
...

@app.route('/about')
def about():
  return render_template("about.html", hello = "Gary Kim")
...
```



about.html 파일 생성은 코드 생성

```html
{% extends "layouts.html" %}
{% block body %}
 
<h1 class="display-4">ABOUT PAGE</h1>
<p class="lead">This Application is build using by python and Flask Framework</p>
<hr class="my-4">
<a class="btn btn-warning btn-lg" href="#" role="button">Learn more</a>
{% endblock %}
```



다음과 같은 페이지 완성

![image-20210419145752412](https://user-images.githubusercontent.com/25717861/115188260-a0470880-a11f-11eb-819d-57c74d44aec7.png)

http://localhost:5000/articles 페이지 구성을 위해서 app.py 에 다음과 같은 코드를 추가한다.

```python
...

@app.route('/articles')
def articles():
  return render_template("articles.html", hello = "Gary Kim")
...
```



about.html 파일 생성은 코드 생성

```html
{% extends "layouts.html" %}
{% block body %}
 
<h1 class="display-4">ARTICLE PAGE</h1>
<p class="lead">This Application is build using by python and Flask Framework</p>
<hr class="my-4">
<a class="btn btn-warning btn-lg" href="#" role="button">Learn more</a>
{% endblock %}
```



다음과 같은 페이지 완성

![image-20210419145903868](https://user-images.githubusercontent.com/25717861/115188387-cec4e380-a11f-11eb-870b-61c95ac4165d.png)

data.py파일에 임의의 MOCKDATA를 만들어 articles에 데이터로 전달하기 위해 

data.py

```python
def Articles():
    articles = [  {  'id': 1,  'title':'Article one',  'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',  'author':'vasanth',  'create_date':'04-09-2018',  }, 
 {  'id': 2,  'title':'Article two',  'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit  in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',  'author':'vasanth nagarajan',  'create_date':'05-09-2018',  },  
{  'id': 3,  'title':'Article three',  'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',  'author':'nagarajan vasanth',  'create_date':'04-09-2018',  } ] 
    return articles
```





app.py 파일에 다음과 같은 코드 추가

```python
...
from data import Articles
...

@app.route('/artcles')
def articles():
    articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = articles)
```



articles 변수로 데이터 전달



artcles.html을 jinja2문법을 사용하여 for문으로 작성 

```html
{% extends "layouts.html" %}
{% block body %}
 
<h1 class="display-4">ARTICLES PAGE</h1>
<p class="lead">This Application is build using by python and Flask Framework</p>
<hr class="my-4">


<table class="table" style="width:100% ">
  <thead class="thead-dark">
  <tr>
    <th scope="col">ID</th>
    <th scope="col">TITLE</th>
    <th scope="col">description</th>
    <th scope="col">AUTHOR</th>
    <th scope="col" >DATE</th>
    <th scope="col" >EDIT</th>
  </tr>
  </thead>
  <tbody>
    {% for article in articles %}
    <tr>
      <th scope="col" >{{article['id']}}</th>
      <td>{{article['title']}}</td>
      <td>{{article['body']}}</td>
      <td>{{article['author']}}</td>
      <td>{{article['create_date']}}</td>
    </tr>
    {% endfor %}
    

  </tbody>
  
  
</table>
<a class="btn btn-warning btn-lg" href="#" role="button">Learn more</a>
{% endblock %}
```






