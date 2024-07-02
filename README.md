import sqlite3

# Establish connection to SQLite database
conn = sqlite3.connect('assignment 3 (12) .db')
cursor = conn.cursor()

# Define User class
class User:
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"{self.first} {self.last} logged in.")

    def logout(self):
        self.logged_in = False
        print(f"{self.first} {self.last} logged out.")

    def search_courses(self):
        # Example of searching courses
        cursor.execute("SELECT * FROM COURSE")
        courses = cursor.fetchall()
        for course in courses:
            print(course)

# Define Student class inheriting from User
class Student(User):
    def __init__(self, first, last, ID, major):
        super().__init__(first, last, ID)
        self.major = major

    def add_class(self, course_id):
        if self.logged_in:
            # Example of adding class for student
            print(f"Added course {course_id} for student {self.first} {self.last}.")
        else:
            print("You must be logged in to add a class.")

    def remove_class(self, course_id):
        if self.logged_in:
            # Example of removing class for student
            print(f"Removed course {course_id} for student {self.first} {self.last}.")
        else:
            print("You must be logged in to remove a class.")

# Define Instructor class inheriting from User
class Instructor(User):
    def __init__(self, first, last, ID, department):
        super().__init__(first, last, ID)
        self.department = department

    def print_course_roster(self, course_id):
        if self.logged_in:
            # Example of printing course roster for instructor
            cursor.execute("SELECT * FROM COURSE_ROSTER WHERE course_id=?", (course_id,))
            roster = cursor.fetchall()
            if roster:
                print(f"Course Roster for Course ID {course_id}:")
                for student in roster:
                    print(student)  # Adjust printing format as per your database schema
            else:
                print(f"No course roster found for course ID {course_id}.")
        else:
            print("You must be logged in to print a course roster.")

# Define Admin class inheriting from User
class Admin(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)

    def add_course_to_schedule(self, course_id):
        if self.logged_in:
            # Example of adding course to semester schedule
            cursor.execute("INSERT INTO SEMESTER_SCHEDULE (course_id) VALUES (?)", (course_id,))
            conn.commit()
            print(f"Added course {course_id} to semester schedule.")
        else:
            print("You must be logged in as admin to add a course to the semester schedule.")

    def remove_course_from_schedule(self, course_id):
        if self.logged_in:
            # Example of removing course from semester schedule
            cursor.execute("DELETE FROM SEMESTER_SCHEDULE WHERE course_id=?", (course_id,))
            conn.commit()
            print(f"Removed course {course_id} from semester schedule.")
        else:
            print("You must be logged in as admin to remove a course from the semester schedule.")

# Example usage:

# Create instances of users
student1 = Student("Alice", "Johnson", 1, "Computer Science")
instructor1 = Instructor("Bob", "Smith", 2, "Physics")
admin1 = Admin("Charlie", "Brown", 3)

# Logging in users
student1.login()
instructor1.login()
admin1.login()

# Perform actions specific to each role
student1.add_class(101)  # Example of adding class for student
instructor1.print_course_roster(101)  # Example of printing course roster for instructor
admin1.add_course_to_schedule(101)  # Example of adding course to semester schedule

# Logging out users
student1.logout()
instructor1.logout()
admin1.logout()

# Close connection to the database
conn.close()
