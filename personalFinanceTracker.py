# ===RICHHY TECH FINANCE TRACKER==
# 1. ADD INCOME
# 2. VIEW EXPENSE
# 3. VIEW SUMMARY
# 5. EXIT

# transaction class
class transaction():
    def __init__(self, type, description, amount, date):
        self.type=type
        self.description=description
        self.amount = amount
        self.date=date

    def get_summary(self):
        print(f"type: {self.type}")
        print(f"desrciption: {self.description}")
        print(f"amount: {self.amount}")
        print(f"date: {self.date}")

    def save_to_file(self):
        with open("personalFinanceTracker.txt", "a") as f:
            f.write(self.get_summary()+ "\n")
        print("transaction has been saved")

def add_income():
    description = input("Enter income source: ")
    amount = int(input("enter amount: "))

    transaction = Transaction({
        "type" : "INCOME",
        "description" : description,
        "amount" : amount
            })
    transaction.save_to_file()
    print("✅income added!")
    

def add_expenses():
    description = input("Enter outgoing expenses: ")
    amount = int(input("Enter amount: "))

    transaction = Transaction({
            "type" : "INCOME",
            "description" : description,
            "amount" : amount
            })
transaction.save_to_file()
print("✅ Expenses added!")

def view_balance():
    try:
        with open("personalFinanceTracker.txt", "r") as f:
        for line in f: