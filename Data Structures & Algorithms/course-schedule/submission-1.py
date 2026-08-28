class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Build the graph
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] +=1

        #Check for prerequestite = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        #Reduce indegrees for next courses
        completed = 0
        while q:
            course = q.popleft()
            completed +=1

            for next_course in graph[course]:
                indegree[next_course] -=1

                if indegree[next_course] == 0:
                    q.append(next_course)
        return completed == numCourses

        