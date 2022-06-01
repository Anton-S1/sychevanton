# программа позволяет записывать студента в таблицу, ставить его средний балл и назначать ему стипендию
import sqlite3
db = sqlite3.connect('database.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
    имя TEXT, курс TEXT, 'средний балл' BIGINT, ' размер стипендии (руб.) ' BIGINT
 )""")
db.commit()

for value in sql.execute("SELECT * FROM students"):
    print(value)
    
student_name = input('Имя студента: ')
student_course = input('Курс: ')
student_score = input('Средний балл:')
student_scholarshp = int(input('Назначте стипендию (в рублях) :'))

sql.execute(f"SELECT имя FROM students WHERE имя =  '{student_name}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO students VALUES (?, ?, ?, ?)", (student_name, student_course, student_score, student_scholarshp))
    db.commit()
else:
    print('Студент уже записан')
    
