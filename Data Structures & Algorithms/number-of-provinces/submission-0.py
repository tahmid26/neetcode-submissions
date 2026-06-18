class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        num_provinces = 0

        def dfs(i):
            visited.add(i)

            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)


        # keep track of number of successful dfs = number of provinces
        for i in range(n):
            if i not in visited:
                num_provinces += 1 
                dfs(i) 

        return num_provinces