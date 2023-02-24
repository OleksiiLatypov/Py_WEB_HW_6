import sqlite3

with open('query_7.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../homework.db') as con:
        cur = con.cursor()
        cur = con.execute(sql)
        return cur.fetchall()

# Знайти оцінки студентів у окремій групі з певного предмета.


for i in execute_query(sql):
    print(*i, sep=', ')