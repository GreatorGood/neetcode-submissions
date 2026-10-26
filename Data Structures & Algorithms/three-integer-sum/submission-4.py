class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        idx = 0
        ans_set = set()

        while(idx<n-2):
            
            
            i = idx+1

            j = n-1
            while(i<j):
                t_sum = nums[idx] + nums[i] + nums[j]
                if t_sum == 0:
                    ans_set.add(tuple(sorted((nums[idx],nums[i],nums[j]))))
                    i += 1
                    j -= 1
                elif t_sum < 0:
                    i += 1
                elif t_sum > 0:
                    j -= 1
            
            idx += 1
        
        return [list(val) for val in ans_set]
            



        
                    



        
        