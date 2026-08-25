class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgemap = [[] for i in range(n)]
        visit = [False] * n

        for a, b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)
        
        def dfs(node):
            for nei in edgemap[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        connected = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                connected+=1
        return connected