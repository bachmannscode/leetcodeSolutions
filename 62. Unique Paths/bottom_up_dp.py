class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 1] = [1] * n
        for row in range(m - 1): dp[row][-1] = 1
        
        for row in range(m - 2, - 1, - 1):
            for col in range(n - 2, - 1, - 1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        
        return dp[0][0]
