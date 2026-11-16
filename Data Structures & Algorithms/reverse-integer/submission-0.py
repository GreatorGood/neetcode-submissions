class Solution:
    def reverse(self, x: int) -> int:
        j = str(x)[::-1]

        if x < 0 : 
            j  = j[:len(j)-1]
            j = int(j) * -1
        else:
            j = int(j)
            
        return j if -2**31 <= j <= 2**31 - 1 else 0