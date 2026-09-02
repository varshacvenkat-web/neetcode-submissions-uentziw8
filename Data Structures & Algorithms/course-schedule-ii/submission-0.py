from collections import defaultdict,deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        in_degree=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        queue=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        order=[]
        while queue:
            course=queue.popleft() #pop from queue
            order.append(course) #add to order
            for j in graph[course]:
                in_degree[j]-=1
                if in_degree[j]==0:
                    queue.append(j)
        if len(order)==numCourses:
            return order
        else:
            return []
