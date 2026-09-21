class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

  

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        node=self.cache[key]
        node.next.prev=node.prev
        node.prev.next=node.next
        #add it to very right bc thats most used 
        node.next=self.right
        node.prev=self.right.prev
        self.right.prev.next=node #pointers the thing before self.right.prev to node 
        self.right.prev=node #then we overwrite the thing before node as node, so then the original node before now pointers to the new node
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #update
            self.cache[key].val=value
            node=self.cache[key]
            #remove
            node.prev.next=node.next
            node.next.prev=node.prev
        else:
            #we make a new node 
            node=Node(key,value)
            self.cache[key]=node 
        #add to the very right 
        node.next=self.right
        node.prev=self.right.prev
        self.right.prev.next=node
        self.right.prev=node 

        if len(self.cache)>self.capacity:
            #left means it was least recently used 
            left=self.left.next #node
            del self.cache[left.key]
            #if we delete this from cache will it sitll be in linked list to reorder poitner
            left.next.prev=self.left
            self.left.next=left.next
       
        
        
        
