class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m = len(s1)
        n = len(s2)

        if m+n != len(s3):
            return False
        

        dp = [ [False] * (m+1)  for _ in range(n+1) ]

        for i in range(m+1):
            if s1[:i] == s3[:i]:
                dp[0][i] = True
        
        for i in range(n+1):
            if s2[:i] == s3[:i]:
                dp[i][0] = True
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                if dp[i-1][j] and s2[i-1] == s3[i+j-1]:
                    dp[i][j] = True

                if dp[i][j-1] and s1[j-1] == s3[i+j-1]:
                    dp[i][j] = True
        
        return dp[n][m]
                
            