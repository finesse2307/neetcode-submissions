class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Build the graph
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] +=1
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0
        while q:
            node = q.popleft()
            taken +=1
            for nxt in graph[node]:
                indegree[nxt] -=1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return taken == numCourses
        
            