
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None 
        stack=[]
        curr=root #curr pointer 
        first=None #first part of linked list
        last=None # last part of linked list 

        while stack or curr:
            while curr: # add all left pointers first
                stack.append(curr)
                curr=curr.left 
        
            curr=stack.pop() #LIFO, pop from very right 
            #now we connect points
            if not last: #nothing has been added yet, we have popped the smallest element 
                first=curr #first itertion
            else:
                last.right=curr #these become the two pointers that we move throughtou the list 
                curr.left=last
            
            last=curr #we keep moving
            curr=curr.right #we check the right pointer, if it exists while curr runs if not we pop the thing in the stack
        last.right=first #connect last and first to make circular 
        first.left=last
        return first





        