
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()
        time =0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -=1
            time +=1
        return time if fresh ==0 else -1