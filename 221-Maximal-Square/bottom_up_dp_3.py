class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        maximum = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    dp[row + 1][col + 1] = 1 + min(dp[row][col + 1], dp[row + 1][col], dp[row][col])
                maximum = max(maximum, dp[row + 1][col + 1])
                
        return maximum*maximum
