"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #DFS approach
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy
            
            for n in node.neighbors:
                copied_neighbor = dfs(n)
                visited[node].neighbors.append(copied_neighbor)

            return visited[node]

        if not node:
            return None
        else:
            clone = dfs(node)

        return clone 