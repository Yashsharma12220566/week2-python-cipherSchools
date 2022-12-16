# In keyword and Iterations in dictionary

user_info = {
    'name' : 'Shivam',
    'age' : 19,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}

# Check if key exist in dictionary  ----->
if 'name' in user_info:
    print('Present')
else:
    print('Not Present')

# Check if value exist in dictionary  ----->
if 'Shivam' in user_info.values():
    print('Present')
else:
    print('Not Present')

if ['coco', 'kimi no na wa'] in user_info.values():
    print('Present')
else:
    print('Not Present')
print("\n")

#                 <---------    Loops In Dictionary    --------->

# Loop for Keys
for i in user_info:
    print(i)
print("\n")

# Loop for values 
for i in user_info.values():
    print(i)

for i in user_info:
    print(user_info[i])
print("\n")

# Keys Method - 
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# Values Method - 
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# Items Method  ----->
user_items = user_info.items()
print(user_items)
print(type(user_items))

# Output - dict_items([('name', 'Shivam'), ('age', 19), ('fav_movies', ['coco', 'kimi no na wa']), ('fav_tunes', ['awakening', 'fairy tale'])])

for key, value in user_info.items():
    print(f"Key is {key} and value is {value}")