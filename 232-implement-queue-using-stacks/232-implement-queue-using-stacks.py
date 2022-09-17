class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()
        
        #Else move all elements from stack_1 to stack_2 and then pop
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()
        
    
    def peek(self) -> int:
        if self.stack_2:
            return self.stack_2[-1]
        
        #Else move all elements from stack_1 to stack_2 and then pop
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]

    def empty(self) -> bool:
        return not bool(self.stack_1) and not bool(self.stack_2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()