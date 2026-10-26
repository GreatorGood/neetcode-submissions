class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = [(val,idx) for idx, val in enumerate(nums)]
        lst.sort(key=lambda x : x[0])

        i = 0
        j = len(nums)-1

        while(i<j):
            if lst[i][0] + lst[j][0] == target:
                return [min(lst[i][1],lst[j][1]),max(lst[i][1],lst[j][1])]
            if lst[i][0] + lst[j][0] > target:
                j -= 1
            if lst[i][0] + lst[j][0] < target:
                i += 1
            
        return []