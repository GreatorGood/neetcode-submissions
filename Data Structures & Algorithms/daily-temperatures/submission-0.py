class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = [0] # store index
        result = [0]*n
        if n == 1:
            return result

        i = 1
        while i < n:
            
            while st and temperatures[i] > temperatures[st[-1]]:
                result[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)                
            i+=1
        

        return result