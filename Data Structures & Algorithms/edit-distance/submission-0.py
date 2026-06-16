class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import sys

        INS_COST = 1
        DEL_COST = 1
        SUB_COST = 1

        n, m = len(word1), len(word2)

        # dp[i][j] = min cost to convert a[:i] -> b[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base cases: convert prefix to empty (deletions) / empty to prefix (insertions)
        for i in range(1, n + 1):
            dp[i][0] = i * DEL_COST
        for j in range(1, m + 1):
            dp[0][j] = j * INS_COST

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost_sub = 0 if word1[i - 1] == word2[j - 1] else SUB_COST

                dp[i][j] = min(
                    dp[i - 1][j] + DEL_COST,          # delete a[i-1]
                    dp[i][j - 1] + INS_COST,          # insert b[j-1]
                    dp[i - 1][j - 1] + cost_sub       # substitute/match
                )

        return dp[n][m]


