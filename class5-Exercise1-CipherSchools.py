# define a function which will take list containing numbers as input
# and return list contaning square of every elements

l2=[]
def square_list(l):
    for i in l:
        n = int(i)**2
        l2.append(n)
    return l2

l = input("Enter list :").split(",")
print(square_list(l))