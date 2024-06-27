



class User:
    #attribute
    
    #constructor
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        
    #methods
    def setFirst(self, first):
        self.first = first
    def setLast(self, last):
        self.last = last
    def setID(self, ID):
        self.ID = ID
    def getInfo(self):
       print("First Name: ", self.first, "\nLast Name: ", self.last, "\nID: ", self.ID )
    def Search(self):
        print("\nCourse")
        cursor.execute("SELECT * FROM COURSE")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
        
   
    def Search_Parameters(self):
        print("Search by parameters was Successfully Used")
        parameter_option = int(input("Select Parameter\n1. CRN (ID)\n2. Title/n3. Department\n4. Time\n5. Weekday\n6. Credits\n7. Exit\n"))
        if parameter_option == 1:
            u_CRN = input("Enter CRN: ")
            cursor.execute("SELECT * FROM COURSE WHERE CRN =?", (u_CRN,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        if parameter_option == 2:
            u_Title = input("Enter Title: ")
            cursor.execute("SELECT * FROM COURSE WHERE TITLE = ?", (u_Title,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        if parameter_option == 3:
            u_DEPT = input("Enter Department: ")
            cursor.execute("SELECT * FROM COURSE WHERE DEPT = ?", (u_DEPT,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        if parameter_option == 4:
            u_Time = input("Enter Time (Ex: 12:30PM): ")
            cursor.execute("SELECT * FROM COURSE WHERE time = ?", (u_Time,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        if parameter_option == 5:
            u_Day = input("Enter Weekdays (Ex: T/TR, M/F): ")
            cursor.execute("SELECT * FROM COURSE WHERE weekday = ?", (u_Day,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        if parameter_option == 6:
            u_Credits = int(input("Enter Number of Credits: "))
            cursor.execute("SELECT * FROM COURSE WHERE credits = ?", (u_Credits,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
class Student(User):
    #attribute
    #constructor
    def __init__(self, first, last, ID):
        User.__init__(self, first, last, ID)
        
    #methods
    def AddDrop(self):
        print("Add/Drop Courses was Successfully Used")
    def Print(self):
        print("Print Schedule was Successfully Used")
       
class Instructor(User):
    #attribute
    #constructor
    def __init__(self, first, last, ID):
        User.__init__(self, first, last, ID)
    
    #methods
    def Print_schedule(self):
        print("Print Schedule was Successfully Used")
    def Print_class(self):
        print("Print Class List was Successfully Used")
 
class Admin(User):
    #attribute
    #constructor
    def __init__(self, first, last, ID):
        User.__init__(self, first, last, ID)
    
    #methods
    def add_remove_courses(self):
        print("Add/Remove Courses was Successfully Used")
    def add_remove_user(self):
        print("Add/Remove Users was Successfully Used")
    def add_remove_student(self):
        print("Add/Remove Student from Course was Successfully Used")
    def roster(self):
        print("Search/Print Roster and Courses was Successfully Used")
        


import sqlite3
conn=sqlite3.connect('assignment3_edit.db')
cursor = conn.cursor()



user_type = int(input('Enter Type of User:\n 1.Student\n 2.Instructor\n 3.Admin\n'))
first_name = input('Enter First Name:\n')
last_name = input('Enter Last Name:\n')
identification = input("Enter Your ID:\n")

if user_type == 1:
    User1 = Student(first_name, last_name, identification)
    print("Welcome ", User1.first, " ", User1.last, " (Student)")
    option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add/Drop Courses\n 3. Print Schedule\n 4. Print Info\n 5. Log Off\n'))
    while option != 5:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User1.Search()
                if search_option == 2:
                    User1.Search_Parameters()
                search_option = int(input('Please Select an Option\n1. Search All Courses\n2. Search by Parameters\n3. Exit\n'))
        if option == 2:
            User1.AddDrop()
        if option == 3:
            User1.Print()
        if option == 4:
            User1.getInfo()
        option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add/Drop Courses\n 3. Print Schedule\n 4. Print Info\n 5. Log Off\n'))
elif user_type == 2:
    User2 = Instructor(first_name, last_name, identification)
    print("Welcome ", User2.first, " ", User2.last, " (Instructor)")
    option = int(input('Please Select an Option\n 1. Search Courses\n 2. Print Class List\n 3. Print Schedule\n 4. Print Info\n 5. Log Off\n'))
    while option != 5:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User2.Search()
                if search_option == 2:
                    User2.Search_Parameters()
                search_option = int(input('Please Select an Option\n1. Search All Courses\n2. Search by Parameters\n3. Exit\n'))
        if option == 2:
            User2.Print_class()
        if option == 3:
            User2.Print_schedule()
        if option == 4:
          User2.getInfo();
        option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add/Drop Courses\n 3. Print Schedule\n 4. Print Info\n 5. Log Off\n'))
elif user_type == 3:
    User3 = Admin(first_name, last_name, identification)
    print("Welcome ", User3.first, " ", User3.last, " (Admin)")
    option = int(input('Please Select an Option\n1. Search Courses\n2. Add/Remove Courses\n3. Add/Remove User\n4. Add/Remove Student\n5. Search/Print Roster and Courses\n6. Print Info\n7. Log Off\n'))
    while option != 7:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User3.Search()
                if search_option == 2:
                    User3.Search_Parameters()
                search_option = int(input('Please Select an Option\n1. Search All Courses\n2. Search by Parameters\n3. Exit\n'))
        if option == 2:
            User3.add_remove_courses()
        if option == 3:
            User3.add_remove_user()
        if option == 4:
            User3.add_remove_student()
        if option == 5:
            User3.roster()
        if option == 6:
           User3.getInfo();
        option = int(input('Please Select an Option\n1. Search Courses\n2. Add/Remove Courses\n3. Add/Remove User\n4. Add/Remove Student\n5. Search/Print Roster and Courses\n6. Print Info\n7. Log Off\n'))
    
print ("Logging Off\n\n")
