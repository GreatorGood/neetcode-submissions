class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        isVisited = [[False]*C for _ in range(R)]
        ans = 0

        def dfs(row,col):

            if(
                row < 0
                or 
                row >= R
                or
                col < 0
                or 
                col >= C
                or
                isVisited[row][col]
                or
                grid[row][col] == '0'
            ):
                return

            isVisited[row][col] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr,dc in directions:
                dfs(row+dr,col+dc)
            



        for r in range(R):
            for c in range(C):
                if not isVisited[r][c] and grid[r][c] == '1':
                    ans += 1
                    dfs(r,c)
        
        return ans