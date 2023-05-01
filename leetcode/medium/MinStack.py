class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # O(1) time | O(1) space
    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    # O(1) time | O(1) space
    def pop(self):
        if len(self.stack) == 0:
            return None
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def top(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    # O(1) time | O(1) space
    def getMin(self):
        return self.min_stack[-1] if len(self.min_stack) > 0 else None


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    assert minStack.pop() == 2
    assert minStack.top() == 1
    minStack.pop()
    minStack.push(5)
    minStack.push(10)
    minStack.push(3)
    minStack.push(8)
    assert minStack.getMin() == 3
