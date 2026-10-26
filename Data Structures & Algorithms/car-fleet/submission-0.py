class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        arr = [(pos,(target-pos)/speed[idx]) for idx,pos in enumerate(position)]
        arr.sort(key=lambda x:x[0])

        ans = n
        top = arr.pop()

        for i in range(n-2,-1,-1):
            if arr[i][1] <= top[1]:
                arr.pop()
                ans -=1
            else:
                top = arr.pop()

        return ans



