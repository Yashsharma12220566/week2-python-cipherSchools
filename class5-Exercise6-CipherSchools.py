# Last Exercise
# define a function to count the no. of list inside the main input list.

# input ---> [1,2,3,4,[1,2],[3,4]]
# output ---> 2
# Hint --> make use of type function

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

l = [1,2,3,4,5,[1,2,3],[4,5]]
print(sublist_counter(l))