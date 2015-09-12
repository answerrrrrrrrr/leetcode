class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or curMin > x:
            curMin = x
        self.stack.append((x, curMin))

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1][0]

    # @return an integer
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]