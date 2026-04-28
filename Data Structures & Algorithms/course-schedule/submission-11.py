class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList={ i:[] for i in range(numCourses)}
        for a,b in prerequisites:
                adjList[b].append(a)
        def dfs(node):
            if node in visit:
                return False 
            elif adjList[node]==[]:
                return True 
            else:
                visit.add(node)
                for neighbor in adjList[node]:
                    if not dfs(neighbor):
                        return False 
                visit.remove(node)
                return True 
        for i in range(numCourses):
            visit=set()
            if not dfs(i):
                return False
        return True 
    
            
