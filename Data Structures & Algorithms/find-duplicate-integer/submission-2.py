class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):

            idx = abs(nums[i])-1  # abs because that value may have been flipped 
            if nums[idx] < 0:
                return idx+1
            else:
                nums[idx] = -1 * nums[idx]

        