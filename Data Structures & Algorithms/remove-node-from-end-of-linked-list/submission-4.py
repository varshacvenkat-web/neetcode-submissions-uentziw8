# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        current=head 
        while current:
            nodes.append(current)
            current=current.next 
        left=len(nodes)-n
        nodes.pop(left)
        if nodes:
            for i in range(len(nodes)-1):
                nodes[i].next=nodes[i+1]
            nodes[-1].next= None 
        return nodes[0] if nodes else None  



            