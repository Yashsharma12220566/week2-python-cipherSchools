# Add and Delete data in Dictionary

user_info = {
    'name' : 'Shivam',
    'age' : 19,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}

# How to add data
user_info['fav_song'] = ['song1','song2']
print(user_info)

# Pop Method  ----->
# user_info.pop()  # gives an error we have write something in pop func.
popped_item = user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")
print(type(popped_item))
print(user_info)

# popitem Method  ------>
popped_item2 = user_info.popitem()
print(f"popped item is {popped_item2}")
print(user_info)
