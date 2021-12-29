"""1.6
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place? 
"""

# tranposition of matrix -> linear algebra
# t: O(n^2)
# s: O(1)
def best_rotate_matrix(matrix: list):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(i + 1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]

# t: O(n^2)
# s: O(n)
def rotate_matrix(matrix: list) -> list:
    """ generalize and expand
    1 0 -> 0 1 -> 0 0 -> 0 0
    0 0    0 0    0 1    1 0

    x x x    x x x
    x     ->     x
    x            x

    intuition:
    create a zero'd copy of nxn matrix
    go from the outside inside of the original matrix
    select each column and just put it in at the rotated space
    """

    n = len(matrix)
    buffer_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for layer in range(n // 2):
        # top = left
        for i in range(layer, n - layer):
            buffer_matrix[layer][i] = matrix[i][layer]

        # right
        for i in range(layer, n - layer):
            buffer_matrix[i][n - layer - 1] = matrix[layer][i]

        # bottom
        for i in range(layer, n - layer):
            buffer_matrix[n - layer - 1][i] |= matrix[i][n - layer - 1]

        # left
        for i in range(layer, n - layer):
            buffer_matrix[i][layer] = matrix[n - layer - 1][i]

    if n % 2 != 0:
        buffer_matrix[n//2][n//2] = matrix[n//2][n//2]
        
    return buffer_matrix

matrix = [[1, 0, 1], [1, 0, 1], [0, 0, 1]]

for row in matrix:
    print(row)

print()
best_rotate_matrix(matrix)

for row in matrix:
    print(row)
# best time O(n^2)

