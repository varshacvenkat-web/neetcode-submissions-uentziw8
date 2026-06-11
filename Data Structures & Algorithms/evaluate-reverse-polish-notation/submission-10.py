class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ("+","-","*","/"):
                a=int(stack.pop())
                b=int(stack.pop())
                if i=="+":
                    x=a+b
                    stack.append(x)
                elif i=="-":
                    y=b-a
                    stack.append(y)
                elif i=="*":
                    z=a*b
                    stack.append(z)
                else:
                    j=int(b/a)
                    stack.append(j)
            else:
                i=int(i)
                stack.append(i)
        return stack.pop()


            