class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely processed
        state = [0] * numCourses

        def dfs(course):
            # We found a cycle
            if state[course] == 1:
                return False

            # Already checked this course
            if state[course] == 2:
                return True

            state[course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True