# Practice for loop
# Ask user a number like 1256
# Calculate sum of digits ----> 1+2+5+6

num = input("Enter a no. : ")
total = 0
for i in range(0,len(num)):
    total += int(num[i])
    
print(total)