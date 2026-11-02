class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(0,0) for _ in range(n+1)]
        dp[0] = (0,0)

        for i in range(n):
            elem = nums[i]

            dp[i+1] = (max(dp[i][1],dp[i][0]),dp[i][0]+elem)
        
        return max(dp[n][0],dp[n][1])
