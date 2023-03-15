class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    s.checkXMatrix(grid)
