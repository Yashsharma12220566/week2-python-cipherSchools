#  Define a function that take list of words as argument and
# return list with reverse of every element in that list

# example
# ['abc', 'tuv', 'xyz'] ---->  ['cba', 'vut', 'zyx']

def rev_elements(l):
    n = []
    for i in l:
        n.append(i[::-1])
    return n

l = input("l: ").split(",")
print(rev_elements(l))