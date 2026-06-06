class Student:
    def __init__(self, name, matric, course, year, gpa): #initializing the information i need to get from the student
        self.name = name
        self.matric = matric
        self.course = course
        self.year = year
        self.gpa = gpa

    # to define the action which the student can do
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Matric: {self.matric}")
        print(f"Course : {self.course}")
        print(f"Year: {self.year}")
        print(f"Gpa: {self.gpa}")
        

    def is_passing(self):
        if float(self.gpa) >= 2.5: # float function to denote float number
            return F"{self.name} is PASSING"
        else:
            return f"{self.name} is FALLING, you need to do bettter and improve"

students=[] #Empty list is to store all students details

# let save student details in a file
def save_students(students):
    with open("students.txt", "a") as f:
        for s in students:
            f.write(f"{s.name} | {s.matric} | {s.course} | year {s.year}|GPA {s.gpa}\n")
    print("\n ALL students saved to students file!")

# ask how many students to register
count = int(input("How many students do you want to register? "))

# get details from user
for i in range(count):
    print("\n === STUDENT REGISTRATION ====")
    print(f"---- Student {i+1} ----")
    name = input("Enter your name: ")
    matric = input("Enter your matric no: ")
    course = input("Enter your course of study: ")
    year = input("Enter your level year: ")
    gpa = input("Enter your GPA: ")

    # get the student info using ther input
    student = Student(name, matric, course, year, gpa)
    students.append(student)

# print all student
print("\n ==== ALL REGISTERED STUDENT ===")
for i in students:
    i.get_info()
    print(i.is_passing())

save_students(students) 