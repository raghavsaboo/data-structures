class Node:

    def __init__(self, val):
        self.data = val
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:

    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def detect_loop(self):
        """
        O(n) Time Complexity
        O(1) Space Complexity
        """
        current = self.head_node
        skip_node = current.next_element

        if skip_node == None:
            return False
        else:
            skip_node = skip_node.next_element


        while current and skip_node and skip_node.next_element:
            if current == skip_node:
                return True
            current = current.next_element
            skip_node = skip_node.next_element.next_element

        return False