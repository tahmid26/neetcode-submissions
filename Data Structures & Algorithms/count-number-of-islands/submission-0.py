# Intuition
# Treat the grid like a map where '1' represents land and '0' represents water.
# Each island is a group of connected land cells.
# When we encounter a land cell, we use BFS to visit all connected land cells and mark them as visited, ensuring the same island is not counted again.

# For DFS approach, just change .popleft() to .pop(). pop from the end (LIFO) instead of the front (FIFO)

# Algorithm
# Traverse every cell in the grid.
# When a '1' (land) cell is found:
# Increment the island count.
# Start BFS from that cell.
# In BFS:
# Push the starting cell into a queue and mark it as visited.
# While the queue is not empty:
# Pop a cell.
# Explore its 4 neighbors (up, down, left, right).
# If a neighbor is land and not visited, mark it as visited  and add it to the queue.
# Continue scanning the grid.
# Return the total number of islands.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = 0


        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row , col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # Boundary conditions & checking if it's water or already visited
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0' or (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                # We only start a BFS if it's land AND we haven't visited it yet
                if grid[r][c] == '1' and (r,c) not in visited: 
                    bfs(r,c)
                    islands += 1
        
        return islands
                

        