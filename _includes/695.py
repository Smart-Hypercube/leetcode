class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = {}
        mapping = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                if i and grid[i-1][j]:
                    islandx, islandy = mapping[i-1, j]
                    mapping[i, j] = islandx, islandy
                    islands[islandx, islandy].add((i-islandx, j-islandy))
                    if j and grid[i][j-1] and mapping[i, j-1] != mapping[i, j]:
                        # join the left side
                        leftx, lefty = mapping[i, j-1]
                        s = islands[islandx, islandy]
                        for (dx, dy) in islands[leftx, lefty]:
                            mapping[leftx+dx, lefty+dy] = islandx, islandy
                            s.add((leftx+dx-islandx, lefty+dy-islandy))
                        del islands[leftx, lefty]
                    continue
                if j and grid[i][j-1]:
                    islandx, islandy = mapping[i, j-1]
                    mapping[i, j] = islandx, islandy
                    islands[islandx, islandy].add((i-islandx, j-islandy))
                    continue
                mapping[i, j] = i, j
                islands[i, j] = {(0, 0)}
        sizes = {len(islands[k]) for k in islands}
        sizes.add(0)
        return max(sizes)
