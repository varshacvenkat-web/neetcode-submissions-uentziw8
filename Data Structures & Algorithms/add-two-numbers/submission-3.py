# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        carry=0
        current1=l1
        current2=l2
        while current1 or current2:
            d1=current1.val if current1 else 0
            d2=current2.val if current2 else 0
            z=d1+d2+carry
            y=z%10
            carry=z//10 #gives tens place 
            k=ListNode(y)
            tail.next=k
            tail=tail.next 
            current1=current1.next if current1 else None 
            current2=current2.next if current2 else None 
        if carry !=0:
                x=ListNode(carry)
                tail.next=x
        return dummy.next
    

    