class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
# Count & Sink

# rcs DFS
    # https://leetcode.com/discuss/40481/python-dfs-solution-o-144ms
    # 144ms
        if not grid or not grid[0]:
            return 0
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    self.destoryIsland(grid, i, j)
        return numOfIslands
    def destoryIsland(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.destoryIsland(grid, i + 1, j)
        self.destoryIsland(grid, i - 1, j)
        self.destoryIsland(grid, i, j + 1)
        self.destoryIsland(grid, i, j - 1)



    # Code Simplified
    # https://leetcode.com/discuss/41509/7-lines-python-14-lines-java
    # 200ms+ (160ms+ <--- m, n = len(grid), len(grid[0]))
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, [i-1, i+1, i, i], [j, j, j-1, j+1])
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))



# itr BFS
    # https://leetcode.com/discuss/31055/python-bfs-solution
    # 100ms+
        # if not grid:
        #     return 0
        # m, n = len(grid), len(grid[0])
        # lands = set([(i,j) for i in range(m) for j in range(n)
        #                 if grid[i][j] == '1'])
        lands = {(i,j) for i,row in enumerate(grid) for j,v in enumerate(row) if v == '1'}

        count = 0
        while lands:
            count += 1
            islandPieces = [lands.pop()]
            while islandPieces:
                i, j = islandPieces.pop()
                for point in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if point in lands:
                        lands.remove(point)
                        islandPieces.append(point)
        return count


























