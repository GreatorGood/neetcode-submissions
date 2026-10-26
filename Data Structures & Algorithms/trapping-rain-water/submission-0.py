class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = heights[0]
        right_max[n-1] = heights[n-1]

        for i in range(1,n):
            left_max[i] = max(left_max[i-1],heights[i-1])

        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],heights[i+1])


        water = 0
        for i in range(n):
            possible_height = min(left_max[i],right_max[i])
            if possible_height > heights[i]:
                water += possible_height-heights[i]
        
        return water
