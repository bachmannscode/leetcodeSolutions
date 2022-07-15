class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        
        def helper(i, j):
            if i == m or j == n: return 0
            if dp[i][j] != 0: return dp[i][j]
            dp[i][j] = helper(i + 1, j) + helper(i, j + 1)
            return dp[i][j]

        return helper(0, 0)
