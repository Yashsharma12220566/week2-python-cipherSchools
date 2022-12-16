# count
# sort method
# sorted function 
# reverse 
# clear
# copy 

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
fruits.sort()
print(fruits)

numbers = [3, 5, 1, 9, 10]
# numbers.sort()   # this will sort the list and again sort it in that variable
print(sorted(numbers))  # but, this sort the list only for that output to print
print(numbers)

# numbers.clear() # it is use to make the list empty 
# print(numbers)

numbers_copy = numbers.copy()
print(numbers_copy)