from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []
        self.top = -1

    def push(self, element=None) -> bool:
        """Push an element onto the stack.

                Args:
                    element: The element to be pushed onto the stack.

                Returns:
                    bool: True if the element was successfully pushed, False otherwise.
                """
        if element is not None:
            self.top += 1
            self.stack.append(element)
            return True
        else:
            return False

    def pop(self) -> Any:
        """Remove and return the top element from the stack.

                Returns:
                    Any: The top element of the stack.
                """
        if self.is_empty():
            return "underflow"
        else:
            self.top -= 1
            top = self.stack[self.top + 1]
            del self.stack[self.top + 1]
            return top

    def peek(self) -> Any:
        """Return the top element from the stack without removing it.
              Returns:
            Any: The top element of the stack.
        """
        return self.stack[self.top]

    def is_empty(self) -> bool:
        # """Check if the stack is empty.
        if self.top == -1:
            return True
        else:
            return False

    def size(self) -> int:
        """Return the number of elements in the stack.

                Returns:
                  int: The number of elements in the stack.
               """
        return len(self.stack)

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self.stack = []  # Reset the stack to an empty list.
        self.top = -1  # Reset the top pointer to -1.


# shalom = MyStack()
# print(shalom.push()) # False
# print(shalom.push(3)) # True
# shalom.push(4)
# int(shalom.peek())#4
# print(shalom.pop())#4
# print(shalom.pop())#3

def check_properly_nested(string: str):
    if len(string) == 0:
        return True
    stack = MyStack()
    for char in string:
        if char in ('(', '{', '['):
            stack.push(char)
        elif char == ')' and stack.peek() == '(':
            stack.pop()
        elif char == '{' and stack.peek() == '}':
            stack.pop()
        elif char == '[' and stack.peek() == ']':
            stack.pop()
        else:
            return False
    return stack.is_empty()


def test(func):
    legals = ['(()[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[][()]]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']
    illegal = ['}}))[{)({]',
               '{)({([)){}',
               '{{}[((]}}]',
               '[){{{{{)}(',
               '{}[[}]}(]{',
               '}[]]{[})[{',
               '][[([}[)()',
               '[)(]){]}(]',
               '(]}}[)})]]',
               '[)((])]{(}']
    for s in legals:
        assert func(s), s
    for s in illegal:
        assert not func(s), s
