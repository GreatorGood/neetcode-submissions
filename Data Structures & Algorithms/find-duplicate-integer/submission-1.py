class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        
        while(i<len(nums)):
            curr_val = nums[i]
            while(curr_val !=i+1):
                temp = nums[curr_val - 1]
                if temp == curr_val:
                    return curr_val
                nums[curr_val - 1] = curr_val 
                curr_val = temp

            else:
                nums[i] = curr_val
                i +=1
        