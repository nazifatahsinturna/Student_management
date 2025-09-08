from Student import Student
class Course:
    def __init__(self, name : str, code : str, instructor : str):
        self.course_name = name
        self.course_code = code
        self.instructor = instructor
        self.students = []
    
    def add_student(self, new_student):
        self.students.append(new_student)

    def display_course_info(self):
        print("Course Information: ")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print("Enrolled Students:", end = " ")
        for student in self.students:
            print(student, end = " ")
        print()

    def __repr__(self): 
        return self.course_name


