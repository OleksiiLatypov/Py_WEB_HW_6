import sqlite3


with open('query_2.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../homework.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# Знайти студента із найвищим середнім балом з певного предмета.

print(*execute_query(sql))