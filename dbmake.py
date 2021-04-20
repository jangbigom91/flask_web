import pymysql

db = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan' 
)

sql = '''
    CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''

# cursor = db.cursor() 는 주석처리 X -> db가 연결되어있어야 하기 때문
# INSERT쿼리를 실행할 때는 cursor.execute(sql), db.commit(), db.close()을 실행. 다른 것은 #처리
# SELECT쿼리를 실행할 때는 cursor.execute('SELECT 쿼리문'), cursor.fetchall(), print(table명?)을 실행. 다른 것은 #처리

sql_1 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네', '최형욱');"
sql_2 = "INSERT INTO `users` (`name`, `email`, `username`, `password`) VALUES ('최정한', 'jangbigom1384@naver.com', 'CHOI', '12345');"
sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);" # input활용


cursor = db.cursor()

# title = input("제목을 적으세요: ")
# body = input("내용을 적으세요: ")
# author = input("누구세요? ")
# 
# input_data = [title, body, author]
# 
# cursor.execute(sql_3, input_data)

# cursor.execute(sql)
# cursor.execute(sql_1)

# cursor.execute(sql_2)
 
# db.commit()
# db.close()

# cursor.execute('SELECT * FROM users;')
cursor.execute('SELECT * FROM topic;')
users = cursor.fetchall()
print(cursor.rowcount, users)