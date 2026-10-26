class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(map(lambda x : str(len(x))+"#"+x,strs))

    def decode(self, s: str) -> List[str]:
        if s == "":
            return list()
        ans = []
        i = 0
        nums = [0,1,2,3,4,5,6,7,8,9]
        while i < len(s):
            slen = 0
            while s[i] != "#":
                n = int(s[i])
                slen = 10*slen + n
                i += 1
            
            ans.append(s[i+1:i+1+slen])
            i += slen+1
        return ans