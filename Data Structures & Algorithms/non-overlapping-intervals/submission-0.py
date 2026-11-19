class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans = 0
        i = 1
        n = len(intervals)
        j = 0
        while i < n:
            if  intervals[i][0] < intervals[j][1]:
                ans += 1
            else:
                j = i
            
            i+=1
        
        return ans