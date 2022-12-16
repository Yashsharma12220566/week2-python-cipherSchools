# filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]

# output ----> [[1,3,5,7], [2,4,6]]

l = [int(i) for i in input("l: ").split(",")]
def odd_even(l):
    n1 = []
    n2 = []
    for i in l:
        if i%2 == 0:
            n2.append(i)
        else:
            n1.append(i)
    return [n1,n2]

print(odd_even(l))