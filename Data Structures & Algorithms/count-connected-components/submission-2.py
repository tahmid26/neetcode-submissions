class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        num_connected = 0
        adj = {}
        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

            return

        for node in range(n):
            if node not in visited:
                num_connected += 1
                dfs(node)

        return num_connected
 
