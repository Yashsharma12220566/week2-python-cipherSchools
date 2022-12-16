# Break and continue Keyword in python

# 1 to 4 print

for i in range(1,11):
    if i == 5:
        break
    print(i)
    
print("\n")
    
# 1 to 10 but without 6

for i in range(0,11):
    if i == 6:
        continue
    print(i)