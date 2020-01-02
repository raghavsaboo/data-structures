class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Full(Exception):
    """Error attempting to access an element from a full container."""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, max_len=20):
        """Create an empty stack."""

        # non-public list instance
        self._capacity = max_len
        self._data = [None]*max_len
        self._n = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self) == 0

    def push(self, e):
        """Add element e to the top of the stack."""

        # new item stored at the end of list
        if self._n == self._capacity:
            raise Full('The stack is full')
        self._data[self._n] = e
        self._n += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self._data[self._n - 1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e. LIFO)

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        
        # remove last item from list
        ans = self._data[self._n - 1]
        self._data[self._n - 1] = None
        self._n -= 1
        return ans 