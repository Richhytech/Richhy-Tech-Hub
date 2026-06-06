# week 7
my_new_list = [1,2,3,4,5,6,7,8,9,10] # using step size
print(my_new_list[::])
print(my_new_list[::2])
print(my_new_list[::-1]) # this will start form the end of the list
print(my_new_list[2:7:-1])
print(my_new_list[-2:-7:-1])

# loops in python
# while and for loops

# while loop
name=input("enter your name: ") # step 1 which is to initailized variable
n = 1
while n <= 10:
    print(f"When n is {n}: print {name}")
    n = n + 1 # or it can be n += 1

table = int(input("Which of the multiplication table: "))
stop = int(input("where to stop: "))
n = 1
while n <= stop:
    result = table * n
    print(f"{table} X {n} = {result}")
    n +=1

# classwork 1
start_num = 1
stop_num = int(input("Enter your stop number: "))
n =1
while n <= stop_num:
    print(n)
    n += 1

# classwork 2
startNum = int(input("Enter your starting even number: "))
stopNum = int(input("Enter your stop even number: "))
n = 2
while n <= stopNum:
    print(n)
    n += 2