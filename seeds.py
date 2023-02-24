from datetime import datetime, timedelta
import faker
from random import randint, choice
import sqlite3
from pprint import pprint

connect = sqlite3.connect("./homework.db")
cur = connect.cursor()

disciplines = ['Історія України',
               "Англійська",
               "Креслення",
               "Дискретна математика",
               "Програмування",
               "Фізика",
               "Органічна хімія"
               ]

groups = ['XK-21', 'XO-01', 'XE-41', 'XM-11']
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

fake = faker.Faker()


def fill_teachers():
    teachers = [fake.name() for i in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    cur.executemany(sql, zip(teachers, ))


def fill_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(?,?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for i in range(len(disciplines)))))


def fill_groups():
    sql = "INSERT INTO groups(name) VALUES(?);"
    cur.executemany(sql, [(i,) for i in groups])


def fill_students():
    students = [fake.name() for i in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for i in range(len(students)))))


def fill_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
    sql = "INSERT INTO grades (discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?)"

    def get_list_date(start, end):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for i in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))
    cur.executemany(sql, grades)


if __name__ == '__main__':
    try:
        fill_teachers()
        fill_disciplines()
        fill_groups()
        fill_students()
        fill_grades()
        connect.commit()
    except sqlite3.Error as error:
        pprint(error)
    finally:
        connect.close()
