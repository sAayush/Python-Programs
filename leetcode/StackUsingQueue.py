class MyStack:
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.queue = []
            
    
        def push(self, x: int) -> None:
            """
            Push element x onto stack.
            """
            self.queue.append(x)
            for i in range(len(self.queue) - 1):
                self.queue.append(self.queue.pop(0))
            
    
        def pop(self) -> int:
            """
            Removes the element on top of the stack and returns that element.
            """
            return self.queue.pop(0)
            
    
        def top(self) -> int:
            """
            Get the top element.
            """
            return self.queue[0]
            
    
        def empty(self) -> bool:
            """
            Returns whether the stack is empty.
            """
            return len(self.queue) == 0
        
        
if __name__ == '__main__':
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
    print(obj.pop())
    print(obj.empty())
    print(obj.push(3))
    print(obj.empty())
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
    print(obj.push(4))
    print(obj.push(5))
    print(obj.push(6))