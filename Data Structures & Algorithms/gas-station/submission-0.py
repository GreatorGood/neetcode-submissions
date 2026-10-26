

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        i = j = 0

        store = 0
        n = len(gas)
        gas.extend(gas)
        cost.extend(cost)

        while i < n :

            if store + gas[j] >= cost[j]:
                store += gas[j] - cost[j]
                j += 1

            else:

                j+= 1
                i = j
                store = 0
            
            if j-i == n:
                return i

        
        return -1



        