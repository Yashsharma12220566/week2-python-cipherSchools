user_info = {
    'name' : 'Shivam',
    'age' : 19,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}

more_info = {'State' : 'Haryana', 'Hobbies' : ['Coding','Reading','Guitar']}

# more_info = {'name' : 'Devraj', 'State' : 'Haryana', 'Hobbies' : ['Coding','Reading','Guitar']}
# If we do this then this new name not added again but it will overwrite the previous one.

user_info.update(more_info)
print(user_info)