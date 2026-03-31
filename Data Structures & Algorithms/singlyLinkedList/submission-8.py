class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):  # ← Fix indentation (4 spaces)
        self.head = Node(0)
    
    def get(self, index: int) -> int:
        cur = self.head.next
        for i in range(index):
            if cur == None:
                return -1
            else:
                cur = cur.next
        
        if cur == None:
            return -1
        return cur.val
    
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
    
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head
        while cur.next != None:  # ← Fix: cur.next, not cur
            cur = cur.next
        cur.next = new_node
    
    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        cur = self.head
        for i in range(index):
            if cur == None:  # ← Fix: == not =
                return False
            else:
                cur = cur.next
        if cur==None:
            return False 
        if cur.next == None:
            return False
        cur.next = cur.next.next
        return True
    
    def getValues(self) -> List[int]:
        results = []
        cur = self.head.next
        while cur != None:
            results.append(cur.val)  # ← Only append value
            cur = cur.next           # ← Then move
        return results               # ← Remove extra append!