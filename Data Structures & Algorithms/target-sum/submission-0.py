class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index: int, current_sum: int) -> int:
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            state = (index, current_sum)
            if state in memo:
                return memo[state]
            
            memo[state] = (
                dfs(index + 1, current_sum + nums[index]) +
                dfs(index + 1, current_sum - nums[index])
            )
            return memo[state]

        return dfs(0, 0)