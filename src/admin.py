import sqlite3

def create_table():
    #SQlite 데이터베이스 파일을 열고 연결 객체 'conn'를 반환, 데이터 파일이 없으면 새로 생성
    conn = sqlite3.connect('game_data.db') 
    #데이터베이스 명령을 실행하기 위해 커서 객체를 생성
    c = conn.cursor()  
    #'users' 테이블을 생성하는 SQL 명령을 실행, id, name, score, level이 있고 'id'는 자동으로 증가하는 기본키
    #테이블이 이미 존재하면 아무 작업도 하지 않는다.
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 score INTEGER NOT NULL,
                 level INTEGER NOT NULL
                 )''')  
    #트랜잭션을 커밋하여 데이터베이스에 변경사항을 저장
    conn.commit()
    #연결 종료
    conn.close()

def save_user_data(name, score, level):
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    #'users' 테이블에 새 레코드를 삽입하는 SQL 명령을 실행
    c.execute("INSERT INTO users (name, score, level) VALUES (?, ?, ?)",
               (name, score, level))
    conn.commit()
    conn.close()

def get_top_scores():
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    #'users' 테이블에서 이름과 점수를 선택하여 점수 순서대로 내림차순으로 정령하고 상위 3개의 레코드를 가져온다.
    c.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 3")
    #쿼리 결과를 모두 가져와서 top_scores에 저장
    top_scores = c.fetchall()  
    conn.close()
    #top_scores가 비어있으면 빈 리스트로 반환
    if not top_scores:
        return []
    return top_scores