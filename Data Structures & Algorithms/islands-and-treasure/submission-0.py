
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        # FIXED: Correct Python len() syntax
        num_rows, num_cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # FIXED: Initialized the queue and visited tracking upfront
        q = deque()
        visited = set()

        # Step 1: Collect ALL treasure chests upfront and put them in the same queue
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        # Step 2: Run a single, unified BFS
        distance = 0
        while q:
            # Snapshot the current size of the queue. 
            # This ensures we process the current "layer" fully before increasing the distance.
            level_size = len(q)
            
            for _ in range(level_size):
                row, col = q.popleft()

                # If it's land, update its value with the current shortest distance
                if grid[row][col] == 2147483647:
                    grid[row][col] = distance

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # Boundary checks & avoiding water/visited cells
                    if nr < 0 or nc < 0 or nr >= num_rows or nc >= num_cols or (nr, nc) in visited or grid[nr][nc] == -1:
                        continue
                    
                    # Mark visited and queue up the next layer
                    visited.add((nr, nc))
                    q.append((nr, nc)) # FIXED: .append() instead of .add()
            
            # Increment distance only after processing the entire current layer
            distance += 1