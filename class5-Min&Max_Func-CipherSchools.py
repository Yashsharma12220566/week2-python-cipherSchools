# Max and Min function

numbers = [6,60,2]
print(min(numbers))
print(max(numbers))

def greatest_diff(l):
    return max(l) - min(l)

l = [int(i) for i in input("l: ").split(",")]
print(greatest_diff(l))