class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        edgemap = {i:[] for i in range(n)}

        for a,b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)
        
        visit = [False] * n
        def dfs(node):
            for nei in edgemap[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                connected+=1
        return connected