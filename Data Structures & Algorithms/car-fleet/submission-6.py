class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        count=0
        for i,j in sorted(zip(position,speed), reverse=True):
                x=(target-i)/j
                if not stack or x>stack[-1]: # we only appned if its greater or equal time. if car behidn is faster, it would catch up so no need to push
                    stack.append(x)
        return len(stack)
    