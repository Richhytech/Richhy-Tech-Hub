from http import client


class Client:
    def __init__(self, Name, Service, Amount, PhoneNumber, PaymentStatus):
        self.Name = Name
        self.Service = Service
        self.Amount = Amount
        self.PhoneNumber = PhoneNumber
        self.PaymentStatus = PaymentStatus

    def get_invoice(self):
        return f"Invoice for {self.Name} - Service: {self.Service} - Amount: N{self.Amount}"

    def make_complaint(self, complaint_text):
        print(f"{self.Name} complained: {complaint_text}")

    def mark_as_paid(self):
        return f"{self.Name} has been marked PAID"

client1 = Client("Emeka", "Logo design", 5000 ,"09124935659", False)

print(client1.get_invoice())
print(client1.make_complaint("Logo colour are fading when zoomed"))
print(client1.mark_as_paid())
print(f"Has {client1.Name} been paid: {client1.PaymentStatus}")