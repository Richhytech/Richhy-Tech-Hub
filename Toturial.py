# # # one value_multiple variable
# # x=y=z="Lion"
# # print(x)
# # print(y)
# # print(z)

# # # unpack a collection
# # animal="lion", "camel", "goat"
# # x,y,z=animal
# # print(x)
# # print(y)
# # print(z)

# # # string slicing
# # b = "hello wolrd!"
# # print(b[2:5])
# # print(b[:5])
# # # negative silicing
# # b = "hello world!"
# # print(b[-5:-2])

# # # case modifictioan
# # a = "Hello World!"
# # print(a.upper())
# # print(a.lower())
# # print(a.capitalize())

# # # formatting string
# # # age=17
# # # #text="I am a boy, and i'm" + age #this is wrong way to conbine string and number
# # # print(text)
# # # let make use of the formst string
# # age=17
# # text="i am a boy, and i'm {}"
# # print(text.format(age))

# # file handling
# # "w"= write(creating new file, deletes old content)
# # "a"=append(addmto existing file, keeps old content)
# # "r" = read(open file to read only)

# # Writing-save a client file
# def save_client(name, service, amount):
#     with open("clients.txt", "a") as f:
#         f.write(f"{name} | {service} | N{amount}\n")
#     print("client saved successfully")
    
# # reading-view all saved clients
# def view_client():
#     with open("clients.txt", "r") as f:
#         print("\n----ALL CLIENTS----")
#         for line in f:
#             print(line.strip())

# # run it
# save_client("Emeka", "Logo design", 5000)
# save_client("Amaka", "typewriting", 3000)
# view_client()

# # OOP(objects oriented programming)
# # CLASS = blank order form template
# # object = one filled order form for one special clients

# # define the template(class)
# class client:
#     # this runs automatically when you create a new client details
#     def __init__(self, name, service, amount, paid):
#         self.name = name
#         self.service = service
#         self.amount = amount
#         self.paid = paid
        
#     # method to print client details
#     def get_summary(self):
#         print(f"Client : {self.name}")
#         print(f"Service : {self.service}")
#         print(f"Amount: N{self.amount}")
#         print(f"Paid : {"paid" if self.paid else "unpaid"}")
#         print("---------------------------------")
        
#     # method to check payment
#     def payment_status(self):
#         if self.paid:
#             return f"{self.name} has paid. Thank you!"
#         else:
#             return f"{self.name} has not paid yet. Send Reminder."
        
# # create objects (fill the form for real clients)
# client1 = client("Emeka", "Logo design", 5000, True)
# client2 = client("Amaka", "copywrite", 30000, True)
# client3 = client("Peace", "web design", 60000, False)
            
# # use them
# client1.get_summary()
# client2.get_summary()
# client3.get_summary()

# print(client1.payment_status())
# print(client2.payment_status())


# comparison value
print(4 <= 1) # false will be the value to answer

# richard = 20
# if richard <=19:
#     print(richard)


# mixing booleans and camparison operators
student = 50
subject = 12
if student == 40 and subject <=12:
    print(student, subject)