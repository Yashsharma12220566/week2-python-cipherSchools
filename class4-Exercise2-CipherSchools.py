# Define is_palindrome function that take one word in string as input 
# and return True if it is palindrome else retuen False

# Palindrome - word that reades same backwards as forwards

# example
# is_palindrome("madam") -----> True
# is_palindrome("naman") -----> True
# is_palindrome("horse") -----> Fasle

# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> compare reversed string with original string

def is_palindrome(word):
    if word[::-1] == word:
        return True
    return False

word = input("Enter a word : ")
print(is_palindrome(word))