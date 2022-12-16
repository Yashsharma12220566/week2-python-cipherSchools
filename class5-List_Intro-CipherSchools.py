# Data structures
# List ----> this chapter
# Ordered collection of items

# You can store anything in lists int, float, string

numbers = [1,2,3,4]
print(numbers)

words = ["word1", "word2", "word3"]
print(words)
print(words[0:2])

mixed = [1, 2, 3, 4, "five", "six", 2.3, None]
print(mixed)
print(mixed[-1])

mixed[1] = "two"
print(mixed)

mixed[1:] = ["Two","Three","Four"]
print(mixed)