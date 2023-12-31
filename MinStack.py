from MyStack import MyStack


class MinStack(MyStack):

    def __init__(self):
        super().__init__()
        self.min = MyStack()

    def push(self, element=None) -> bool:
        if element is not None:
            self.top += 1
            self.stack.append(element)
            if self.min.is_empty() or element < self.min.peek():
                self.min.push(element)
            return True
        return False

    def pop(self):
        if self.is_empty():
            return "underflow"
        else:
            self.top -= 1
            top = self.stack[self.top + 1]
            del self.stack[self.top + 1]
            if top == self.min.peek():
                self.min.pop()
            return top

    def get_min(self):
        return self.min.peek()

    def clear(self):
        super().__init__()
        self.min.clear()
