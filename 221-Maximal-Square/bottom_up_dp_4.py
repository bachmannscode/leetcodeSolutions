class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * (len(matrix[0])) for _ in range(len(matrix))]
        maximum = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    maximum = max(maximum, 1)
                    if row != 0 and col != 0:
                        dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                        maximum = max(maximum, dp[row][col])
                    else:
                        dp[row][col] = int(matrix[row][col])
                
        return maximum*maximum
