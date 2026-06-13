class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        count=0
        for i,j in sorted(zip(position,speed), reverse=True): #we sort by position(sort does it from least to greatest, but we reverse to greatest to least)
                x=(target-i)/j #time=(distance/rate)
                if not stack or x>stack[-1]: #append if stack empty
                    stack.append(x)          #when we start greatest postiio's time gets appneded, then we check 2nd greatest. If that time catches up then we don't append if x is same or less as it would be in the same fleet. If x is greater it appends as a new fleet. we do this for each value and check with previosu as fleet can only be made with the previous car ahead, so each time we have ot check with the car bfore.
        return len(stack)
    
    