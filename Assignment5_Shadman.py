import sqlite3

# Establish connection to SQLite database
conn = sqlite3.connect('assignment3_edit.db')
cursor = conn.cursor()

class User:
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        self.logged_in = False
        
    def login(self):
        self.logged_in = True
        print("Logged In\n")
    
    def setFirst(self, first):
        self.first = first
        
    def setLast(self, last):
        self.last = last
        
    def setID(self, ID):
        self.ID = ID
        
    def getInfo(self):
        print("First Name: ", self.first)
        print("Last Name: ", self.last)
        print("ID: ", self.ID)
        
    def Search(self):
        print("\nCourse")
        cursor.execute("SELECT * FROM COURSE")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
            
    def Search_Parameters(self):
        print("Search by parameters was Successfully Used")
        parameter_option = int(input("Select Parameter\n1. CRN (ID)\n2. Title\n3. Department\n4. Time\n5. Weekday\n6. Credits\n7. Exit\n"))
        if parameter_option == 1:
            u_CRN = input("Enter CRN: ")
            cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (u_CRN,))
        elif parameter_option == 2:
            u_Title = input("Enter Title: ")
            cursor.execute("SELECT * FROM COURSE WHERE TITLE = ?", (u_Title,))
        elif parameter_option == 3:
            u_DEPT = input("Enter Department: ")
            cursor.execute("SELECT * FROM COURSE WHERE DEPT = ?", (u_DEPT,))
        elif parameter_option == 4:
            u_Time = input("Enter Time (Ex: 12:30PM): ")
            cursor.execute("SELECT * FROM COURSE WHERE TIME = ?", (u_Time,))
        elif parameter_option == 5:
            u_Day = input("Enter Weekdays (Ex: T/TR, M/F): ")
            cursor.execute("SELECT * FROM COURSE WHERE WEEKDAY = ?", (u_Day,))
        elif parameter_option == 6:
            u_Credits = int(input("Enter Number of Credits: "))
            cursor.execute("SELECT * FROM COURSE WHERE CREDITS = ?", (u_Credits,))
        elif parameter_option == 7:
            return
        else:
            print("Invalid option.")

        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

class Student(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)
        
    def AddCourse(self):
        print("Add Course was Successfully Used")
        course_id = input("Enter the course ID to add: ")
        cursor.execute("INSERT INTO ENROLLMENT (student_id, course_id) VALUES (?, ?)", (self.ID, course_id))
        conn.commit()
        print(f"Course {course_id} added to your schedule.")
        
    def RemoveCourse(self):
        print("Remove Course was Successfully Used")
        course_id = input("Enter the course ID to remove: ")
        cursor.execute("DELETE FROM ENROLLMENT WHERE student_id = ? AND course_id = ?", (self.ID, course_id))
        conn.commit()
        print(f"Course {course_id} removed from your schedule.")

    def Print(self):
        print("Print Schedule was Successfully Used")
        cursor.execute("SELECT COURSE.* FROM COURSE JOIN ENROLLMENT ON COURSE.CRN = ENROLLMENT.course_id WHERE ENROLLMENT.student_id = ?", (self.ID,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

class Instructor(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)

    def Print_schedule(self):
        print("Print Schedule was Successfully Used")
        cursor.execute("SELECT * FROM COURSE WHERE instructor_id = ?", (self.ID,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
    
    def Print_class(self):
        print("Print Class List was Successfully Used")
        course_id = input("Enter the course ID to print the roster: ")
        cursor.execute("SELECT STUDENT.* FROM STUDENT JOIN ENROLLMENT ON STUDENT.ID = ENROLLMENT.student_id WHERE ENROLLMENT.course_id = ?", (course_id,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

class Admin(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)

    def add_courses(self):
        print("Add Courses was Successfully Used")
        u_id = input("Enter CRN: ")
        u_title = input("Enter Title: ")
        u_DEPT = input("Enter DEPT (4 Characters): ")
        u_time = input("Enter time (Ex: 8:00AM): ")
        u_week = input("Enter weekdays (Ex: M/F): ")
        u_semester = input("Enter semester: ")
        u_year = input("Enter year: ")
        u_credits = input("Enter credits: ")
        cursor.execute("INSERT INTO COURSE (CRN, TITLE, DEPT, TIME, WEEKDAY, SEMESTER, YEAR, CREDITS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                       (u_id, u_title, u_DEPT, u_time, u_week, u_semester, u_year, u_credits))
        conn.commit()
        print(u_title + " was successfully added\n")

    def remove_courses(self):
        print("Remove Courses was Successfully Used")
        u_id = input("Enter CRN: ")
        cursor.execute("DELETE FROM COURSE WHERE CRN = ?", (u_id,))
        conn.commit()
        print("Course with CRN " + u_id + " was deleted\n")

    def add_remove_student(self):
        print("Add/Remove Student from Course was Successfully Used")
        action = input("Would you like to add or remove a student? (add/remove): ").strip().lower()
        student_id = input("Enter the student ID: ")
        course_id = input("Enter the course ID: ")
        if action == 'add':
            cursor.execute("INSERT INTO ENROLLMENT (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
            conn.commit()
            print(f"Student {student_id} added to course {course_id}.")
        elif action == 'remove':
            cursor.execute("DELETE FROM ENROLLMENT WHERE student_id = ? AND course_id = ?", (student_id, course_id))
            conn.commit()
            print(f"Student {student_id} removed from course {course_id}.")
        else:
            print("Invalid action.")

    def roster(self):
        print("Search/Print Roster and Courses was Successfully Used")
        course_id = input("Enter the course ID to print the roster: ")
        cursor.execute("SELECT STUDENT.* FROM STUDENT JOIN ENROLLMENT ON STUDENT.ID = ENROLLMENT.student_id WHERE ENROLLMENT.course_id = ?", (course_id,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

# Main code to handle user input
user_type = 0
while user_type == 0:
    first_name = input('Enter First Name:\n')
    last_name = input('Enter Last Name:\n')
    identification = input("Enter Your ID:\n")

    cursor.execute("SELECT * FROM STUDENT WHERE ID = ?", (identification,))
    if cursor.fetchone():
        user_type = 1
        print("Logged In\n")
        
    cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?", (identification,))
    if cursor.fetchone():
        user_type = 2
        print("Logged In\n")
        
    cursor.execute("SELECT * FROM ADMIN WHERE ID = ?", (identification,))
    if cursor.fetchone():
        user_type = 3
        print("Logged In\n")
        
    if user_type == 0:
        print("Failed Login. Re-Enter Information\n")

if user_type == 1:
    User1 = Student(first_name, last_name, identification)
    User1.login()
    print("Welcome ", User1.first, " ", User1.last, " (Student)")
    option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add Course\n 3. Remove Course\n 4. Print Schedule\n 5. Print Info\n 6. Log Off\n'))
    while option != 6:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n 3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User1.Search()
                elif search_option == 2:
                    User1.Search_Parameters()
                search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n 3. Exit\n'))
        elif option == 2:
            User1.AddCourse()
        elif option == 3:
            User1.RemoveCourse()
        elif option == 4:
            User1.Print()
        elif option == 5:
            User1.getInfo()
        option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add Course\n 3. Remove Course\n 4. Print Schedule\n 5. Print Info\n 6. Log Off\n'))
        
