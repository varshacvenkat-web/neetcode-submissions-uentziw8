# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next 
class Linkedlist:
    def __init__(self):
        self.head=ListNode(0)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None 
        current=head 
        while current !=None:
            next_temp=current.next 
            current.next=prev
            prev = current 
            current=next_temp
        return prev
        


        