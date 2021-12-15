import sqlite3

conn = sqlite3.connect("game.db")
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE game (
# pgn text,
# closing_vote_time text
# )""")
