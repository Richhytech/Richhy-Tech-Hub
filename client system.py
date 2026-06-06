def save_clients(name, service):
    with open("clients.txt", "a") as f:
        f.write(name + "|" + service +"\n")
    print("clientb details have been saved")

def view_clients():
    with open("clients.txt", "r") as f:
        for line in f:
            print(line)
            
name=input("Enter your name: ")
service=input("Enter service order: ")
save_clients(name, service)
view_clients()