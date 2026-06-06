# def add_vat(amount):
#     return amount * 1.075
# print(add_vat(5000)) # using normal def function

# # but if i were to use lambda shortcut of this it will be
# add_vat = lambda amount: amount * 1.075
# print(add_vat(5000))

# # normal input function
# name = input("Enter your full name: ")
# print(name)

# but for the chortcut it will be
get_name = lambda: input("Enter your name: ")
name = get_name
print(name) 