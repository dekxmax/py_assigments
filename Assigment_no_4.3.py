import sqlite3

conn = sqlite3.connect("db_1.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE new_stud(
st_id VARCHAR(30) primary key ,
NAME varchar(60),
CLASS varchar(30)

)
""")

cursor.execute("""
CREATE TABLE new_empl(
emp_id VARCHAR(30) primary key ,
NAME varchar(60),
post  char(30)

)
""")
cursor.execute("""
INSERT into student(st_id,NAME,CLASS)values
("101","Sachin","12th"),
("102","sanat","12th")
""")
cursor.execute("""
INSERT into employee(emp_id,NAME,post)values
("11","Sagar","HR"),
("12","khan","engg.jr")
""")

cursor.execute("""
SELECT * from student               
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""
SELECT * from employee             
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("""
UPDATE student SET NAME = "Vipul"
where st_id = "102"
""")

cursor.execute("""
DELETE from employee
where emp_id = "12"
""")
conn.commit()
conn.close()