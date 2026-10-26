import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))

        ans = [abs(heap[0][0])]
        for i in range(k,n):
            heapq.heappush(heap,(-nums[i],i))
            while heap[0][1] <= i-k:
                heapq.heappop(heap)
            
            ans.append(-heap[0][0])
        
        return ans
            
