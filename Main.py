from Student import Student
from Course import Course
import json

student_data = {} #dictionaries to maintain objects
course_data = {}
def menu(): #function for menu
    print()
    print("1. Add New Student")
    print("2. Add New Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade for Student")
    print("5. Display Student Details")
    print("6. Display Course Details")
    #print("7. Save data to File") these should be auto
    #print("8. Load Data from file")
    print("0. Exit")
    try:
      choice = int(input("Select Option: "))
    except ValueError:
        return None 
    return choice

def add_student(student_data): #function for adding a student in the dictionary
    name = input("Enter Name: ")
    age = -1
    while True: #checking for correct input
        try:
           age = int(input("Enter Age: "))
           if age < 0:
               raise ValueError()
           break
        except ValueError:
            print("Age must be a positive integer. Please try again.")
    add = input("Enter Address: ")
    while True:
        id = input("Enter Student ID: ").upper()
        if student_data.get(id) == None: #making sure the id is unique
            st = Student(name, age, add, id)
            student_data[id] = st
            print(f"Student {name} (ID: {id}) added successfully.")
            break
        else:
            print("A student with this ID already exists. Please try again")
    
def add_course(course_data): #function for adding a course in the dictionary
    course_name = input("Enter Course Name: ")
    code = ''
    while True: #making sure the course code is unique
        code = input("Enter Course Code: ").upper()  
        if course_data.get(code) == None:
            break
        else:
            print("A couse with this code already exists. Please Try Again.")
    instructor =  input("Enter Instructor's Name: ")
    cr = Course(course_name, code, instructor)
    course_data[code] = cr
    print(f"Course {course_name} (Code: {code}) created with Instructor {instructor}")

def enroll_student(student_data, course_data): # function for enrolling the student
    id = input("Enter Student ID: ").upper()
    course_code = input("Enter Course code: ").upper()
    st = student_data.get(id)
    cr = course_data.get(course_code)
    if st != None and cr != None:
        st.enroll_course(cr)
        cr.add_student(st)
        print(f"Student {st} (ID: {id}) enrolled in {cr} (Code: {course_code})")
    else:
        print("Either the student, the course, or both do not exist.")

def assign_grade(student_data, course_data):#function for assigning grade
    id = input("Enter Student ID: ").upper()
    course_code = input("Enter Course code: ").upper()
    grade = input("Enter Grade: ").upper()
    st = student_data.get(id)
    cr = course_data.get(course_code)
    if st != None and cr != None:
        print(st.courses)
        if cr in st.courses: #checking whether student is enrolled in the course or not
            st.add_grade(cr.course_name, grade)
            print(f"Grade {grade} added for {st} in {cr}.")
        else:
            print("Student is not enrolled in the course")
    else:
        print("Either the student, the course, or both do not exist.")

def save_data(student_data, course_data):
    st_dict = {}
    cr_dict = {}

    for id, student in student_data.items(): #converting student object to dictionaries
        st_dict[id] = {
            "name" : student.name,
            "age" : student.age,
            "address" : student.address,
            "grades" : student.grades,
            "courses" : [course.course_code for course in student.courses]
            }
   
    for code, course in course_data.items(): #converting course object to dictionaries
        cr_dict[code] = {
            "course name" : course.course_name,
            "instructor" : course.instructor,
            "students" : [student.student_id for student in course.students]
        }

    st_data = json.dumps(st_dict)
    cr_data = json.dumps(cr_dict)

    with open("student_details.json", "w") as f: #opening in writing mode
        f.write(st_data)

    with open("course_details.json", "w") as f: #opening in writing mode
        f.write(cr_data)

    
    #print("All student and course data saved successfully.")

def load_data(student_data, course_data):
    st_dict = {}
    cr_dict = {}
    try: 
        with open("student_details.json", "r") as f:
            data = f.read()
            st_dict = json.loads(data)
    except FileNotFoundError:
        pass

    try: 
        with open("course_details.json", "r") as f:
            data = f.read()
            cr_dict = json.loads(data)
    except FileNotFoundError:
        pass
    
    for id, student in st_dict.items(): #creating student objects from json
        st = Student(student["name"], student["age"], student["address"], id)
        st.grades = student["grades"]
        student_data[id] = st

    for code, course in cr_dict.items(): #creating course objects from json
        cr = Course(course["course name"], code, course["instructor"])
        course_data[code] = cr

    for id, student in st_dict.items(): #enrolling students
        st = student_data.get(id)
        codes = student["courses"] #list of course codes
        for code in codes:
            cr = course_data.get(code)
            st.enroll_course(cr)
            cr.add_student(st)    

    #print("Data loaded successfully.")


print("==== Student Management System ====")
load_data(student_data, course_data) #loading data at the begining
while True:
    choice = menu()
    print()
    if choice == 0:
        print("Exiting Student Managent System. Goodbye!")
        break
    elif choice == 1:
        add_student(student_data)
    elif choice == 2:
        add_course(course_data)
    elif choice == 3:
        enroll_student(student_data, course_data)
    elif choice == 4:
        assign_grade(student_data, course_data)
    elif choice == 5:
        id = input("Enter Student ID: ").upper()
        st = student_data.get(id)
        if st != None:
            st.display_student_info()
        else:
            print("Student doesn't exist.")
    elif choice == 6:
        code = input("Enter Course code: ").upper()
        cr = course_data.get(code)
        if cr != None:
            cr.display_course_info()
        else:
            print("Course doesn't exist.") 
    # elif choice == 7:
    #     save_data(student_data, course_data)
    # elif choice == 8:
    #     load_data(student_data, course_data)     
    else: #if user enters anything other than the given choices
        print("Input not valid. Kindly choose one of the available options")

save_data(student_data, course_data) # saving data at the end of the program so we don't loose any information
