class Solution:
    def shiftGrid(self, grid, k):
        arr = []
        for row in grid:
            for num in row:
                arr.append(num)
        n = len(arr)
        k %= n
        arr = arr[-k:] + arr[:-k]
        ans = []
        cols = len(grid[0])
        for i in range(0, n, cols):
            ans.append(arr[i:i + cols])
        return ans