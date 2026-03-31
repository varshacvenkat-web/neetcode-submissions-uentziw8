# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        tail=head 
        while list1 !=None and list2!=None:
            if list1.val==list2.val:
                tail.next=list1
                list1=list1.next 
                tail=tail.next 
            elif list2.val==list1.val:
                tail.next=list2
                list2=list2.next
                tail=tail.next
            elif list1.val>list2.val:
                tail.next=list2
                tail=tail.next 
                list2=list2.next
            elif list1.val< list2.val:
                tail.next=list1 
                list1=list1.next 
                tail=tail.next 
        if list1==None:
            tail.next=list2
        if list2==None:
            tail.next=list1
        
        
            
    
        return head.next

        