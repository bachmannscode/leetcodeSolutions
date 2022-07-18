class Solution:
    def maximalSquare(self, matrix):
        maximum = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    matrix[row][col] = 1 + min(int(matrix[row][col - 1] if col != 0 else 0), int(matrix[row - 1][col - 1] if row != 0 else 0), int(matrix[row - 1][col] if row != 0 and col != 0 else 0))
                    maximum = max(maximum, matrix[row][col])

        return maximum ** 2
