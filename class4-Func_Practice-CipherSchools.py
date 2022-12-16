# Functions Practice

def last_letter(x):
    return x[-1]

x = input("Enter a word : ")
print(last_letter(x))
# last_letter(8)  #error

def odd_even(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"


# def odd_even(num):
#     if num%2 == 0:
#         return "Even"
#     return "Odd"

num = int(input("Enter a number : "))
print(odd_even(num))


# def is_even(num1):
#     if num1%2 == 0:
#         return True
#     return False

def is_even(num1):
    return num1%2 == 0
print(is_even(9))

def song():
    return "happy birthday song"
print(song())