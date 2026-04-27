class Graph:
    
    def __init__(self):
        self.adjList={}


    def addEdge(self, src: int, dst: int) -> None:

            if src not in self.adjList:
                self.adjList[src]=[]
            if dst not in self.adjList:
                self.adjList[dst]=[]
            self.adjList[src].append(dst)



    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList:
            if dst in self.adjList[src]:
                self.adjList[src].remove(dst)
                return True 
            else:
                return False 
        return False 


    def hasPath(self, src: int, dst: int) -> bool:
        visit=set()
        def dfs(node,target,adjList,visit):
            if node in visit: 
                return False
            if node==target:
                return True 
            visit.add(node)
            for neighbor in self.adjList[node]:
                if dfs(neighbor,target,adjList,visit):
                    return True 
            return False 
        return dfs(src,dst,self.adjList,visit)

