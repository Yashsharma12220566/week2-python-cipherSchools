# list inside list

matrix = [[1,2,3],[4,5,6],[7,8,9]]     # 2d list
# 3 items ---> 3 list
# print(matrix[2])

for sublist in matrix:
    for i in sublist:
        print(i, end = " ")
print("\n")
print(matrix[2][0])
print(matrix[0][2])

s = "string"
print(type(s))
print(type(matrix))