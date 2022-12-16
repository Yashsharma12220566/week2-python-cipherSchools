# common elements finder function
# define a functions which take 2 lists as input and return a list
# which contains common elements of both lists

# example
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

l1 = [int(i) for i in input("l1: ").split(",")] 
l2 = [int(x) for x in input("l2: ").split(",")]

def common_elements(l1,l2):
    l3 = []
    for i in l1:
        for j in l2:
            if i == j:
                l3.append(j)
    return l3

print(common_elements(l1,l2))