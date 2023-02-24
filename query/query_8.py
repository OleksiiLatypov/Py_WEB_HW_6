import sqlite3

with open('query_8.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../homework.db') as con:
        cur = con.cursor()
        cur = con.execute(sql)
        return cur.fetchall()

# Знайти середній бал, який ставить певний викладач зі своїх предметів.

print(*execute_query(sql))