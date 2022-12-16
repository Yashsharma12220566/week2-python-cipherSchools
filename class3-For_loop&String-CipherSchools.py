name = "Harshit"
for i in range(len(name)):
    print(name[i])
print("\n")

name = "harshit"
for i in name:
    print(i)
print("\n")

for i in "mohit":
    print(i)
print("\n")

# 12356 ---> 1+2+3+5+6
num = input("Enter a number : ")
total = 0
for i in num:
    total += int(i)
print(total)
