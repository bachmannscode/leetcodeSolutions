class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        maximum = 0
        
        for row in range(len(matrix)):
            for bit in range(len(matrix[0])):
                if matrix[row][bit] == "1":
                    dp[row + 1][bit + 1] = 1 + min(dp[row][bit + 1], dp[row + 1][bit], dp[row][bit])
                maximum = max(maximum, dp[row + 1][bit + 1])
                
        return maximum*maximum
