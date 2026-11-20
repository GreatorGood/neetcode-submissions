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

        """
        Code Explanation:
        - State: (index, current_sum) tracks our position in `nums` and the running total so far.
        - Base Case: Once `index == len(nums)`, return 1 if `current_sum == target` (valid expression), else 0.
        - Memoization: `memo` caches solved `(index, current_sum)` states so overlapping branches return in O(1).
        - Transitions: At each index, branch into `+nums[index]` and `-nums[index]` and sum their valid ways.
        - Complexity: O(n * S) time and space, where n = len(nums) and S = sum(nums) (at most n * (2S + 1) unique states).
        """