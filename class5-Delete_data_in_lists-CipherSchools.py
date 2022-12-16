# common methods to delete data from list 

fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']

# pop method
# fruits.pop()   # as default pop remove the last index item
# print(fruits)
# fruits.pop(1)
# print(fruits)

# del method
# del fruits[1]
# print(fruits)

# remove method
fruits.remove('pear')
fruits.remove('apple')  # here, it will remove only the first similar item from the list
print(fruits)

