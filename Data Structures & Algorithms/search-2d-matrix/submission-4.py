class Solution:
    def row_col_idx(self,num,m,n):
        return (num//n,num%n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n-1

        while(low<=high):

            mid = (low+high)//2
            r,c = self.row_col_idx(mid,m,n)
            elem = matrix[r][c]

            if elem < target:
                low = mid +1
            elif elem > target:
                high = mid - 1
            else:
                return True
        
        return False
