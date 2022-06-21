class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0 
        def bfs(i,j):
            q = deque([(i,j)])
            while q: 
                I,J = q.popleft() 

                for _i,_j in [I-1,J], [I,J-1], [I+1,J], [I,J+1]:
                    if 0<=_i<len(grid) and 0<=_j<len(grid[0]) and grid[_i][_j]=='1':
                        grid[_i][_j]='0'
                        q.append((_i,_j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    bfs(i,j)
                    count+=1 
        
        return count
                    
        