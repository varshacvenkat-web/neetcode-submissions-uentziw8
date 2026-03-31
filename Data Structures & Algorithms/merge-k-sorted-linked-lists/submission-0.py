# Definition for singly-linked list.
class ListNode:
 def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

class Solution:  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None  
        results=lists[0]  
        for i in range(1,len(lists)):
            head=ListNode(0)
            current=head
            p1=results
            p2=lists[i]
            while p1 and p2:
                if p1.val<=p2.val:
                    current.next=p1
                    current=current.next
                    p1=p1.next 
                else:
                    current.next=p2
                    current=current.next 
                    p2=p2.next 
            if p1!=None and p2==None:
                current.next=p1
            if p2!=None and p1==None:
                current.next=p2 
            results=head.next 
        return results   
                
        