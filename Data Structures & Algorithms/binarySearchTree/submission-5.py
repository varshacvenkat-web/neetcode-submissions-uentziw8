class TreeNode:
    def __init__(self,key: int, val: int, left=None, right=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right

class TreeMap:
    
    def __init__(self):
        self.root=None
  

    def insert(self, key: int, val: int) -> None:
        curr=self.root
        parent=None 
        while curr!=None:
            parent=curr
            if key<curr.key:
                curr=curr.left
            elif key>curr.key:
                curr=curr.right
            else:
                curr.val=val
                return None  
        newnode=TreeNode(key,val)
        if parent==None:
            self.root=newnode
        elif key<parent.key:
            parent.left=newnode 
        else:
            parent.right=newnode
        


    def get(self, key: int) -> int:
        curr=self.root
        while curr!=None:
            parent=curr
            if key<curr.key:
                curr=curr.left
            elif key>curr.key:
                curr=curr.right
            else:
                return curr.val 
        return -1 


    def getMin(self) -> int:
        curr=self.root
        if not self.root:
            return -1 
        while curr!=None:
            parent=curr
            curr=curr.left 
        return parent.val

    def getMax(self) -> int:
        curr=self.root
        if not self.root:
            return -1 
        while curr!=None:
            parent=curr
            curr=curr.right 
        return parent.val 
    def remove(self, key:int)-> None:
        self.root=self._remove(self.root,key) #starts search at root 


    def _remove(self, node, key: int) -> None:
        if node is None: 
            return None
        elif key<node.key:
            node.left=self._remove(node.left,key)
        elif key>node.key:
            node.right=self._remove(node.right,key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            #inorder processor 
            curr=node.right 
            while curr.left:
                curr=curr.left 
            node.key=curr.key
            node.val=curr.val 
            node.right = self._remove(node.right, curr.key)
        return node 
        




    def getInorderKeys(self) -> List[int]:
        result=[]
        self.inorder(self.root, result)
        return result 
    def inorder(self, node, result):
        if not node:
            return 
        self.inorder(node.left,result)
        result.append(node.key)
        self.inorder(node.right,result)
        return result
        

    
    # base case?
    # recurse left
    # append
    # recurse right

      
        

