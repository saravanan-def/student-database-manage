


import pymysql

try:
    # Conntect to MySql
    conn = pymysql.connect(
        user='root',
        password='root',
        host='localhost',
        database='students_db'
    )
    cursor = conn.cursor()
    print("Connected to MySQL database !")

except mysql.connector.Error as err:
    print("Failed to connect to MySQL database.",err)
    conn = None
    cursor = None

cursor = conn.cursor()

def add_student(Roll_num,Name,age,Grade):
    sql = "INSERT INTO students(Roll_num,Name,age,Grade) Values(%s,%s,%s,%s) "
    Values = (Roll_num,Name,age,Grade)
    cursor.execute(sql,Values)
    conn.commit()
    print("Student Added Successfully!")

def view_student():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_student(Roll_num,Name,age,Grade):
    sql = " UPDATE students SET Name=%S,age=%S,Grade=%S WHERE Roll_num=%s "
    Values = (Roll_num,Name,age,Grade)
    cursor.execute(sql,Values)
    conn.commit()
    print("Student Updated Successfully!")

def delete_student(Roll_num):
    sql = "DELETE FROM students WHERE Roll_num=%s"
    cursor.execute(sql,(Roll_num,))
    conn.commit()
    print("Student Deleted Successfully!")

# Menu Driven Program
while True:
    print("\n----- Student Datebase Management ------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Roll_num = int(input("Enter Student Roll Number: "))
        Name = str(input("Enter Student Name: "))
        Age = int(input("Enter Student Age: "))
        Grade = str(input("Enter Student Grade: "))
        add_student(Roll_num,Name,Age,Grade)

    elif choice == 2:
        view_student()

    elif choice ==3:
        Roll_num = int(input("Enter Student Roll Number to Update : "))
        Name = str(input("Enter Student New Name: "))
        Age = int(input("Enter Student New Age: "))
        Grade = str(input("Enter Student New Grade: "))
        update_student(Roll_num, Name, Age, Grade)

    elif choice ==4:
        Roll_num = int(input("Enter Student Roll Number To Delete : "))
        delete_student(Roll_num)

    elif choice ==5:
        print("Exiting...... \n Thank You!")
        break
    else:
        print("Invalid Choice, Try Again! ")

