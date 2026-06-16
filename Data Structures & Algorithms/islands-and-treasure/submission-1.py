
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        num_rows, num_cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
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


# If you put all the ancestors (Generation 0) into a queue, the queue will look like this:
# q = [ChestA, ChestB, ChestC]

# When you ask Python for level_size = len(q), it returns 3.

# The line for _ in range(level_size): tells the program: "Pop and process exactly 3 items from the queue right now, and absolutely DO NOT increase the distance counter until all 3 are finished."

# Step-by-Step Execution Trace
# Let’s watch how the queue and the distance counter move together during a search:

# 1. Layer 0 (Distance = 0)
# At the start, q = [ChestA, ChestB, ChestC].

# level_size = len(q) sets level_size to 3.

# The for loop runs exactly 3 times. It pops ChestA, ChestB, and ChestC.

# As it processes them, it finds their neighbors (who are all 1 step away) and appends them to the back of the queue.

# q now looks like this: [Child1, Child2, Child3, Child4, Child5].

# The for loop finishes. The code finally moves past the loop and hits distance += 1. Distance is now 1.