class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.items = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.items.append(x)

    # @return nothing
    def pop(self):
        if not self.empty():
            self.items.pop(0)

    # @return an integer
    def peek(self):
        return self.items[0]

    # @return an boolean
    def empty(self):
        return not len(self.items)
        
