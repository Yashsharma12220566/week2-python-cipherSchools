# Looping inside tuples
# Tuple with one element
# Tuple without paranthesis
# Tuple unpacking
# List inside tuple
# Some functions that you can use with tuples

mixed = (1,2,3,4,0)

# for loop on tuple  ------>

for i in mixed:
    print(i)
# NOTE - You can use while loop too

# tuple with one element  ----->
# nums = (1)   gives an error but,
nums = (1,)    # not give any error so for one element tuple you have to place a comma after the element
words = ('word1')
print(type(words))  # gives string
words = ('word1',)
print(type(words))  # gives tuple

# Tuple without parenthesis  ------>
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

# Tuple unpacking ------>
guitarists = ('Maneli Jamal', 'Eddie van der meer', 'Andrew Foy')
guitarists1,guitarists2,guitarists3 = (guitarists)
print(guitarists2)

# List inside Tuple  ------>
favorites = ('southern mangolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)

# Min, Max and Sum  ----->
print(min(mixed))
print(max(mixed))
print(sum(mixed))