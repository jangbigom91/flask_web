from flask import Flask, render_template, request, redirect
from data import Articles
import pymysql

app = Flask(__name__)

# 웹페이지에 오류가 뭔지 나타남. 나중에 배포할 때는 app.debug를 지워주고 배포해야됨. True로 하면 해킹당할 수 있음.
app.debug = True

# Database 연결
db = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan' 
)

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
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = topics)

@app.route('/article/<int:id>')
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods = ["GET", "POST"])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title  = request.form['title']
        desc   = request.form['desc']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);" # input활용
        input_data = [title, desc, author]
        
        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()
        
        return redirect("/articles")
    
    # return "<h1>글쓰기 페이지</h1>"
    
    else:
        return render_template("add_articles.html")

@app.route('/delete/<int:id>', methods = ["POST"])
def delete(id):
    cursor = db.cursor()
    # sql = 'DELETE FROM `topic` WHERE id = %s;' # 두가지 방법 %s, format
    # id = [id]
    # cursor.execute(sql, id)
    
    sql = 'DELETE FROM `topic` WHERE id = {}'.format(id)
    cursor.execute(sql)

    db.commit()
    
    return redirect("/articles")

@app.route('/<int:id>/edit', methods = ["GET", "POST"])
def edit(id):
    if request.method == "POST":
        return "Success"
    
    else:
        return render_template("edit_article.html")



# 프로젝트 시작점, 먼저 실행함
if __name__ == '__main__':
    app.run()