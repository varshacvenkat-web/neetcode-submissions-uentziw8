class ListNode:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None 
class Deque:
    
    def __init__(self):
        self.head=ListNode(1)
        self.tail=ListNode(1)
        self.head.next=self.tail
        self.tail.prev=self.head


    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True 
        else:
            return False 
        

    def append(self, value: int) -> None:
        newnode=ListNode(value)
        newnode.next=self.tail 
        newnode.prev=self.tail.prev
        self.tail.prev.next=newnode
        self.tail.prev=newnode
        

    def appendleft(self, value: int) -> None:
        newnode=ListNode(value)
        newnode.next=self.head.next
        newnode.prev=self.head
        self.head.next.prev=newnode
        self.head.next=newnode
        

    def pop(self) -> int:
        if self.head.next==self.tail:
            return -1
        else:
            save=self.tail.prev.value
            self.tail.prev=self.tail.prev.prev
            self.tail.prev.next=self.tail
        return save
        

    def popleft(self) -> int:
        if self.head.next==self.tail:
            return -1
        else:
            save=self.head.next.value 
            self.head.next=self.head.next.next 
            self.head.next.prev=self.head
        return save
        
