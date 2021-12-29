"""1.8
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O. 

base cases:
if len < 1:
    return 

create a buffer array to set the new array
iterate over each element keeping track of the row and column,
if we identify a zero update the buffer array
set the old array to the buffer array
"""

def zero_matrix(matrix: list):
    if len(matrix) < 1:
        return

    n = len(matrix)
    m = len(matrix[0])

    buffer = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            buffer[i][j] = matrix[i][j]

    for i in range(n):
        for j in range(m):
            element = matrix[i][j]

            if element == 0:
                for k in range(m):
                    buffer[i][k] = 0
                for l in range(n):
                    buffer[l][j] = 0 

    for i in range(n):
        for j in range(m):
            matrix[i][j] = buffer[i][j]

# t O(n * m)
# s O(n) 

matrix = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0]]

for row in matrix:
    print(row)

print("!!checking for 0's!!")
zero_matrix(matrix)

for row in matrix:
    print(row)