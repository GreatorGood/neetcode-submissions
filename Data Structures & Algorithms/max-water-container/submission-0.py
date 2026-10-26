class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        arr = [(val,idx) for idx,val in enumerate(heights)]
        arr.sort(key=lambda x:x[0])

        ans = 0

        i = 0
        for j in range(len(heights)-1,-1,-1):
            if i == n:
                break
            while(i<n and arr[i][0]<=heights[j]):
                ans = max(ans,(abs(j-arr[i][1]))*arr[i][0])
                i+=1
        
        i = 0
        for k in range(len(heights)):
            if i ==n:
                break
            while(i<n and arr[i][0]<=heights[k]):
                ans = max(ans,(abs(k-arr[i][1]))*arr[i][0])
                i+=1
        
        return ans
            


