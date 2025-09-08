#import Course
class Person:
    def __init__(self, name : str, age : int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person): #it inherits from person class
    def __init__(self, name : str, age : int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject : str, grade : str):
        self.grades[subject] = grade

    def enroll_course(self, new_course):
        self.courses.append(new_course)

    def display_student_info(self):
        print("Student Information: ")
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:", end = " ")
        for course in self.courses:
            print(course, end = " ")
        print()
        print("Grades:", self.grades)


    def __repr__(self): 
        return self.name

# s1 = Student("Anika", 32, "Dhaka", "2001")
# s1.display_student_info()

