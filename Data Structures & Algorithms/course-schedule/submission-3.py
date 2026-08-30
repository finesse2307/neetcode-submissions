class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Build the graph
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            indegree[course] +=1
            graph[pre].append(course)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        completed = 0
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                completed +=1
                for nxt in graph[node]:
                    indegree[nxt] -=1
                    if indegree[nxt] == 0:
                        q.append(nxt)
        return numCourses == completed
        
            