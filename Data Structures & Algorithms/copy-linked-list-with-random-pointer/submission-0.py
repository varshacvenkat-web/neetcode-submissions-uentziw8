"""
 Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dicts={}
        current=head
        while current:
            dicts[current]=Node(current.val) #extract the value and stoere in dictionary as current: value
            current=current.next 
        current=head 
        while current:
            copied_node=dicts[current] #extracts current node: value, which has the next and random nodes attached
            copied_node.next=dicts[current.next] if current.next else None 
            copied_node.random=dicts[current.random] if current.random else None 
            current=current.next
        return dicts[head] if head else None 
        