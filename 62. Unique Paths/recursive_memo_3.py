class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        
        def helper(i, j):
            if dp[i][j] != 0: return dp[i][j]
            dp[i][j] = (helper(i + 1, j) if i + 1 != m else 0) + (helper(i, j + 1) if j + 1 != n else 0)
            return dp[i][j]

        return helper(0, 0)
