class Solution:
    def __init__(self):
        self.result = 0
    
    def dfs(self, grid, visited, x, y):
        if grid[x][y] == '1':
            grid[x][y] = '2'
            if(y+1 < len(grid[x])):
                if grid[x][y+1] == '1':
                    visited.append((x, y+1))
            
            if(y-1 >= 0):
                if grid[x][y-1] == '1':
                    visited.append((x, y-1))
            
            if(x-1 >= 0):
                if grid[x-1][y] == '1':
                    visited.append((x-1, y))
            
            if(x+1 < len(grid)):
                if grid[x+1][y] == '1':
                    visited.append((x+1, y))
        if(visited):
            cur = visited.pop(0)
            
            self.dfs(grid, visited, cur[0], cur[1])
        else:
            return
    
    def numIslands(self, grid):
        visited = []
        for x in range(0,len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] == '1':
                    self.result +=1
                    
                    self.dfs(grid, visited, x, y)
        return self.result

if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))