class Tree:
    """Abstract base class representing a tree structure.
    """

    class Node:
        """An abstraction representing the location of a single element.
        """
        def element(self):
            """Return th element stored at this Node."""
            raise NotImplementedError('must be implemented by subclass.')

        def __eq__(self, other):
            """Return True if other Node represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)

    def root(self):
        """Return Node representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, n):
        """Return Node representing n's parent (or None if n is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, n):
        """Return the number of children that Node n has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, n):
        """Generate an iteration of Nodes representing n's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, n):
        """Return True if node n represents the root of the tree"""
        return self.root() == n

    def is_leaf(self, n):
        """Return True if node n does not have any children."""
        return self.num_children(n) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, n):
        """Return the number of levels separating Node n from the root."""
        if self.is_root(n):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree."""
        # Works but is O(n^2) worst-case time
        return max(self.depth(n) for n in self.positions() if self.is_leaf(p))

    def _height2(self, n):
        """Return the height of the subtree rooted at Position n"""
        # Time is linear in size of substree - O(n)
        if self.is_leaf(n):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(n))

    def height(self, n=None):
        """Return the height of the subtree rooted at Node n.

        If n is None, return the height of the entire tree.
        """
        if n is None:
            n = self.root()
        return self._height2(n)