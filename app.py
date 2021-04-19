from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

# 웹페이지에 오류가 뭔지 나타남. 나중에 배포할 때는 app.debug를 지워주고 배포해야됨. True로 하면 해킹당할 수 있음.
app.debug = True

# 경로설정, ex) 기본경로 뒤에 data를 추가, http://localhost:5000/data
@app.route('/', methods=['GET'])
def index():
    # return "Hello World"
    return render_template("index.html", data="CHOI")

@app.route('/about')
def about():
    return render_template("about.html", hello = "Gary Kim")

@app.route('/articles')
def articles():
    articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = articles)

@app.route('/article/<int:id>')
def article(id):
    print(id)
    return "Success"

# 프로젝트 시작점, 먼저 실행함
if __name__ == '__main__':
    app.run()