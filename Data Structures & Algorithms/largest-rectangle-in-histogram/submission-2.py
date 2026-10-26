class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = [0] * len(heights)
        n = len(heights)

        def traverse(arr,reverse=False):

            left_st = [0]

            ans = arr[0]

            for i in range(1,len(arr)):
                height = arr[i]

                if height > arr[left_st[-1]]:
                    
                    left_st.append(i)
                    
                else:
                    
                    while(left_st and arr[left_st[-1]]>=height):
                        left_st.pop()
                        
                    
                    
                    if left_st:
                        area[n-i-1 if reverse else i] += (i-left_st[-1]-1)*height
                    else:
                        area[n-i-1 if reverse else i] += (i)*height
                    
                    left_st.append(i)
                    
            
        traverse(heights)
        traverse(list(reversed(heights)),reverse=True)
        for i in range(len(heights)):
            area[i] += heights[i]
        return max(area)
        