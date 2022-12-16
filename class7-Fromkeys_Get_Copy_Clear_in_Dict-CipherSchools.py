# FromKeys  ----->

# d = {'name' : 'unknown', 'age' : 'unknown'}

d = dict.fromkeys(range(1,11), 'unknown')
print(d)

d = dict.fromkeys("abc", 'unknown')
print(d)

d = dict.fromkeys(('name', 'age', 'address'), 'unknown')
print(d)

d = dict.fromkeys(['name', 'age', 'address'], ['unknown', 'unknown'])
print(d)


# Get Method  ------->

d = {'name' : 'Shivam', 'age' : 'unknown'}
# print(d['name'])
# print(d[names])   give an error

print(d.get('name'))
#  But print(d.get('names'))   not give an error it just return NONE

# if 'name' in d:
#     print('Present')
# else:
#     print('Not Present')

if d.get('age'):
    print('Present')
else:
    print('Not Present')


# Clear Method   ------->

# d.clear()
# print(d)


# Copy Method   ------->
d1 = d.copy()    # these are different dictionaries
# d1 = d      # these are same dictionaries in this if we apply pop on d1 but data will pop from both dictionaries but if we use copy method then this problem doesn't occur.
print(d1)
print(d1 is d)