import collections 

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = collections.defaultdict(list)
        
        for (a, b) , val in zip(equations, values):
            graph[a].append([b , val])
            graph[b].append([a, 1 / val])


        def dfs(src, tar, visited):
            if src == tar:
                return 1
            
            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei,tar, visited)
                    if res != -1:
                        return res * weight
            
            return -1

        res = []
        for src , tar in queries:
            if src not in graph or tar not in graph:
                res.append(-1)
            else:
                res.append(dfs(src, tar, set()))
        return res




        