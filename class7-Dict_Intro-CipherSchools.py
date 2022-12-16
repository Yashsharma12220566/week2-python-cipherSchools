# Dictionaries Intro
# Q - Why we use dictionaries?
# A - Because of limitations od lists, lists are not enough to represent real data

# Example

user = ['Harshita', 24, ['coco', 'kimi no na wa'],['awakening', 'fairy tale']]
#  This list contains user nam, age, fav_movies, fav_tunes
# You can do this but this is not a good way to do this.

# Q - What are dictionaries
# A - Unordered collections of data in key : value pair.

# How to create dictionaries   ----->
user = {'name':'Harshit', 'age':24}
print(user)
print(type(user))
# print(user[0])    it gives an error
print(user['name'])
print(user['age'])

# Second method to create dictionary  ----->
user1 = dict(name = 'Harshit', age = 24)
print(user1)
print(type(user1))

# How to access data from dictionary
# NOTE - There is no indexing bacause of unordered collections of data

# Which type of data a dictionary can store ?
# Anything ---- Numbers, list, tuple, dictionary.

user_info = {
    'name' : 'Shivam',
    'age' : 19,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}

print(user_info)

# How to add data to empty dictionary  ------>

user_info2 = {}
user_info2['name'] = 'Shivam'
user_info2['age'] = 19
print(user_info2)