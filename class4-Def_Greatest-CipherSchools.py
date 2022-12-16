def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest(100,40,30))
num1 = int(input("Number1 : "))
num2 = int(input("Number2 : "))
num3 = int(input("Number3 : "))
great = greatest(num1,num2,num3)
print(f"{great} is the Greatest number.")