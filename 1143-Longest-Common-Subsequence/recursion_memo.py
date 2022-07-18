class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2): return 0
            if dp[i1][i2] != -1: return dp[i1][i2]
            if text1[i1] == text2[i2]: dp[i1][i2] = 1 + helper(i1 + 1, i2 + 1)
            else: dp[i1][i2] = max(helper(i1, i2 + 1), helper(i1 + 1, i2))
            return dp[i1][i2]

        return helper(0, 0)
