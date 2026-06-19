class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0


        def bfs(r, c):
            q = deque()
            area = 0

            visited.add((r,c))
            q.append((r,c))
            area += 1


            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))
                    area +=1

            return area



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    if area > maxArea:
                        maxArea = area
        
        return maxArea


        
        