class MyStack:

    def __init__(self):
        self.queue=[]

        
        

    def push(self, x: int) -> None:
        self.queue.append(x)

        

    def pop(self) -> int:
        for i in range(len(self.queue)-1):
            x=self.queue.pop(0)
            self.queue.append(x)
        return self.queue.pop(0)

        

    def top(self) -> int:
        for i in range(len(self.queue)):
            x=self.queue.pop(0)
            self.queue.append(x)
            if i == len(self.queue)-1:
                return x

        

    def empty(self) -> bool:
        if self.queue==[]:
            return True
        else:
            return False 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()