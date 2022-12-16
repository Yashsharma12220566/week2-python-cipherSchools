# Functions

name = "harshit"
print(len(name))  # len function

def add_two(a,b):
    return a+b

# total = add_two(10,4)
# print(total)

print(add_two(10,4))

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
total = add_two(a,b)
print(total)

first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
total = add_two(first_name,last_name)
print(total)
