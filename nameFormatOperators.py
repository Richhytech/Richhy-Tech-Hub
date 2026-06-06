# take first, middle and last name
firstName = input("Enter first name: ")
middleName = input("Enter middle name: ")
lastname = input("Enter Surname name: ")
txt="My name is {} {} {}, i'm {} years older"
age=19

full_name=firstName+ " " + middleName + " " + lastname # using concatenent string
print(full_name)

print(txt.format(firstName, middleName, lastname, age)) # using format string