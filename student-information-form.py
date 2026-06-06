# student information
name = input("Enter Student's name: ")
age = int(input("Enter Student's age: "))
grade = float(input("Enter Student's grade: "))

# grade checking for student
if grade >= 90:
    print(f"{name} has an A grade")
elif grade >= 80:
    print(f"{name} has an B grade")
elif grade >= 70:
    print(f"{name} has an c grade")
elif grade >= 60:
    print(f"{name} has an D grade")
else:  print(f"{name} has an F grade")

print(f"{name} is {age} years old and has a grade of {grade}.")