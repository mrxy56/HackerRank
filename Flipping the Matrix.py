# It can be proved that you can change among the diagonal elements without changing the others by drawing the matrix.
def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(matrix[i][j], matrix[2 * n - 1 - i][j], matrix[i][2 * n - 1 - j], matrix[2 * n - 1 - i][2 * n - 1 - j])
    return ans