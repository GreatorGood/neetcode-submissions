class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo  = {}
        def solve(i):
            if i == n-1:
                return True
            
            if nums[i] == 0:
                return False
            
            for jump in range(nums[i],0,-1):
                if i+jump >= n:
                    continue
                if (i+jump) not in memo:
                    res = solve(i+jump)
                    memo[i+jump] = res
                else:
                    res = memo[i+jump]
                
                if res:
                    return True
                
            
            return False
        
        return solve(0)