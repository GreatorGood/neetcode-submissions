from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        total_cnt = 0
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
            total_cnt += 1
        
        for c in t:
            if chars[c] == 0:
                return False
            else:
                chars[c] -=1
                total_cnt -= 1
        
        if total_cnt == 0:
            return True
        else:
            return False

        