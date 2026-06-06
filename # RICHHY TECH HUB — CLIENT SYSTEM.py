# RICHHY TECH HUB — CLIENT SYSTEM
# Uses: Dictionary + File Handling + OOP together
from datetime import date
today=date.today()
print(today)

class Client:
    def __init__(self, name, service, amount, paid, today):
        # details is a DICTIONARY
        self.name = name
        self.service = service
        self.amount = amount
        self.paid = paid
        self.today = today
        
    def get_summary(self):
        status = "Paid" if self.paid else "Unpaid"
        return f"{self.name} | {self.service} | N{self.amount} | {status} | {self.today}"

    def save_to_file(self):
        with open("richhy_clients.txt", "a") as f:
            f.write(self.get_summary() + "\n")
        print(f"{self.name} saved to file!")


# YOUR TASKS — complete these yourself:

# TASK 1: Create a dictionary for a new client
# called "Blessing" who ordered "Instagram Post design"
# for N4000 and has not paid yet
# YOUR CODE HERE
client_dict={
    "name": "Blessing",
    "service": "Instragram post design",
    "amount": 4000,
    "paid": False,
    "today": today
    }
# for key,value in client.items():
#     print(key, ":", value)
# TASK 2: Create a Client object using that dictionary
# YOUR CODE HERE
client1 = Client(**client_dict)

# TASK 3: Call get_summary() and print it
# YOUR CODE HERE
print(client1.get_summary())

# TASK 4: Call save_to_file() to save the client
# YOUR CODE HERE
def save_to_file(self):
    with open("richhy_clients.txt", "a") as f:
        f.write(self.get_summary() +"\n")
    print(f"{self.name} saved a new file!")
    
# TASK 5: Create 2 more clients using dictionaries
# and save them all to the file
# YOUR CODE HERE
client1_dict={
    "name": "Alex",
    "service": "Facebook post design",
    "amount": 8000,
    "paid": True,
    "today": today
    }
client2_dict={
    "name": "Joshua",
    "service": "Social media design",
    "amount": 4000,
    "paid": True,
    "today": today
    }
client1 = Client(**client1_dict)
client2 = Client(**client2_dict)

client1.save_to_file()
client2.save_to_file()
# TASK 6: Write a function called view_all_clients()
# that opens richhy_clients.txt and prints every line
# YOUR CODE HERE
     
def view_all_client():
    try:
        with open("richhy_clients.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileExistsError:
        print("No Client found.")
view_all_client()

def seacrh_client():
    name = input("Enter client name to search: ")
    try:
        with open("richhy_clients.txt", "r") as f:
            for line in f:
                if name in line:
                    print(line.strip())
                    break
            else:
                print(f"{name} not found.")
    except FileExistsError:
        print("No Client found.")
seacrh_client()