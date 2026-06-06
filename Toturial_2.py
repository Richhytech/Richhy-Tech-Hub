# dictionary example
client = {
    "name" : "richard",
    "service" : "Logo design",
    "Amount": 5000,
    "paid" : False
}

# read from ir or print it out
print(client["name"])
print(client["service"])
# add a new key
client["phone"] = "09124935659"

#update an existing key
client["Amount"] = 3000

# Print everything together
for key, value in client.items():
    print(key, ":", value)