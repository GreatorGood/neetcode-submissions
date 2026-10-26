class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 1
        ans = 0
        max_h = max(heights)
        while(i<=max_h):
            curr_ans = 0
            width = 0
            for height in heights:
                if height >= i:
                    width+=1
                else:
                    curr_ans = max(curr_ans, width*i)
                    width=0

            curr_ans = max(curr_ans, width*i)
            ans = max(curr_ans, ans)
            i+=1

        
        return ans

        