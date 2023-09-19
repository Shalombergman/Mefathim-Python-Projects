from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self):
        """Initialize an empty stack."""

    def push(self, element=None) -> bool:
        """Push an element onto the stack.

        Args:
            element: The element to be pushed onto the stack.

        Returns:
            bool: True if the element was successfully pushed, False otherwise.
        """

    def pop(self) -> Any:
        """Remove and return the top element from the stack.

        Returns:
            Any: The top element of the stack.
        """

    def peek(self) -> Any:
        """Return the top element from the stack without removing it.

        Returns:
            Any: The top element of the stack.
        """

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """

    def size(self) -> int:
        """Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """

    def clear(self) -> None:
        """Remove all elements from the stack."""
