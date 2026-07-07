import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visiting = set()
        visited = set()

        for a,b in prerequisites:
            graph[a].append(b)


        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for nei in graph[course]:
                
                if not dfs(nei):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


            





        