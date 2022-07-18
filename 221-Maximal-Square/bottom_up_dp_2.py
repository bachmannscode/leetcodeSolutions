class Solution:
    def maximalSquare(self, matrix):
        maximum = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    maximum = max(maximum, 1)
                    if col != 0 and row != 0:
                        matrix[row][col] = 1 + min(int(matrix[row][col - 1]), int(matrix[row - 1][col - 1]), int(matrix[row - 1][col]))
                        maximum = max(maximum, matrix[row][col])

        return maximum ** 2
