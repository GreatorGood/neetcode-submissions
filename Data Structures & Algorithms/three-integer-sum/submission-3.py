class Solution:
    def bs(self,arr,i,j,target):
        low = i
        high = j
        while(low<=high):
            mid = (low+high)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
        
        return None
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans_set = set()
        i = 0
        n = len(nums)
        

        while(i<n-2):
            
            j = n-1
            left_end = i+1
            while(j>1):

                res = self.bs(nums,left_end,j-1,-(nums[i]+nums[j]))

                if res:
                    ans_set.add(tuple(sorted((nums[i],nums[j],nums[res]))))
                    left_end = res+1
                
                j -=1

            i+=1
        
        return [list(elm) for elm in ans_set]
                    



        
        