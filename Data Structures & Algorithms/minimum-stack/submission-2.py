class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack=[]

    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))
        self.stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
