class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={} #cache is a hashmap so we can store key and value and look up key at o(1)
        self.left=Node(0,0)#dummy nodes
        self.right=Node(0,0)#dummy node
        self.left.next=self.right
        self.right.prev=self.left 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            #remove node
            node=self.cache[key] #goes to the node with that key o(1)
            node.prev.next=node.next
            node.next.prev=node.prev
            #insert at very end (because that shows its most recently used in cache)
            node.prev=self.right.prev
            node.next=self.right
            self.right.prev.next=node
            self.right.prev=node
            return self.cache[key].val #retyrbs value but because its a node its .val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val=value 
             #remove node
            node=self.cache[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            #insert at very end (because that shows its most recently used in cache)
            node.prev=self.right.prev
            node.next=self.right
            self.right.prev.next=node
            self.right.prev=node
        else:
            node=Node(key,value) #we make a new node 
            self.cache[key]=node #we use key to add in hashmap and set equal to new node, so we can look up by key
          #add to MRU
            node.prev=self.right.prev
            node.next=self.right
            self.right.prev.next=node
            self.right.prev=node
            #if over capacity remove the last key
            if len(self.cache)>self.capacity:
                lru=self.left.next
                del self.cache[lru.key]
                self.left.next=lru.next
                lru.next.prev=self.left
        
