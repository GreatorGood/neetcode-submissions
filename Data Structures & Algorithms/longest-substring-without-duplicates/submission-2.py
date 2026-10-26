class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        cur_len = 1
        i = 0
        j = 1
        n = len(s)
        st = set()
        st.add(s[0])
        while(j<n):
            if s[j] not in st:
                st.add(s[j])
                cur_len += 1
                
            else:
                ans = max(ans,cur_len)
                while(s[i]!=s[j]):
                    st.discard(s[i])
                    i+=1
                    cur_len -=1
                else:
                    i+=1
                    
                
            j+=1

        return max(ans,cur_len)

        