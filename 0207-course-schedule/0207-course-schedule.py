class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        path = set()
        visit = set()
        def dfs(course):
            if course in path:
                return False
            if course in visit:
               return True
            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            path.remove(course)
            visit.add(course)
            return True
            
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True
        

        