import sqlite3

def get_top_scores():
    conn = sqlite3.connect('game_data.db')
    c = conn.cursor()
    c.execute("SELECT name, score FROM users ORDER BY score DESC LIMIT 3")
    top_scores = c.fetchall()
    conn.close()
    return top_scores