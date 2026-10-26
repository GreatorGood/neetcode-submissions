class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(1,len(matrix)):
            matrix[0].extend(matrix[i])
        
        arr = matrix[0]
        low = 0
        high = len(arr)-1

        while(low<=high):

            mid = (low+high)//2
            elem = arr[mid]

            if elem < target:
                low = mid +1
            elif elem > target:
                high = mid - 1
            else:
                return True
        
        return False
