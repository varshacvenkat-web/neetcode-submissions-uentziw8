# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        groupprev=dummy
        dummy.next=head 
        groupstart=head
        while True:
            if groupstart == None:
                return dummy.next
            kth=groupstart
            for m in range(k-1): #1.next, 2.next
                kth=kth.next 
                if kth==None:
                    return dummy.next
            i=groupstart
            j=None 
            for n in range(k):
                temp=i.next #save i.next
                i.next=j #rewire next
                j=i #move j forward 
                i=temp #move i forward 
        
            groupstart.next=i #node 4
            groupprev.next=j #node 3
            groupprev=groupstart #set groupprev=node 1
            groupstart=i #set group start equal to node 3
        return dummy.next


