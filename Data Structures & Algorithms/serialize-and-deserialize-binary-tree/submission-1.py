# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        queue=deque()
        output=[]
        output.append(root.val)
        queue.append(root)
        while queue:
            x=queue.popleft()
            if x.left:
                queue.append(x.left)
                output.append(x.left.val)
            else:
                output.append("Null")
            if x.right:
                queue.append(x.right)
                output.append(x.right.val)
            else:
                output.append("Null")
        return ",".join([str(i) for i in output])
        


        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return None 
        values=data.split(",") #we split the string
        root=TreeNode(int(values[0])) #convert to int 
        queue=deque() #make queue
        queue.append(root) #append root 
        i=1 #position of value
        while i<len(values): 
            x=queue.popleft()
            if values[i]=="Null":
                x.left=None 
            else:
                x.left=TreeNode(int(values[i]))
                queue.append(x.left)
            i+=1
            if values[i]=="Null":
                x.right=None 
            else:
                x.right=TreeNode(int(values[i]))
                queue.append(x.right)
            i+=1
        return root 
            
                



