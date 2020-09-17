class Node:

    def __init__(self, data):
        self.data = data
        self.next_element = None


class SinglyLinkedList:

    def __init__(self):
        self.head_node = None

    def get_head(self):
        """
        O(1) time complexity
        O(1) space complexity
        """
        return self.head_node

    def is_empty(self):
        """
        O(1) time complexity
        O(1) space complexity
        """
        if self.head_node == None:
            return True
        else:
            return False

    def __str__(self):
        """
        O(n) time complexity
        O(n) space complexity
        """
        if (self.is_empty()):
            return "List is Empty"

        output = ""
        temp = self.head_node

        while temp.next_element != None:
            output = output + str(temp.data) + "-->"
            temp = temp.next_element

        output = output + str(temp.data) + "-->None"

        return output

    def __len__(self):
        """
        O(n) time complexity
        O(1) space complexity
        """

        current = self.head_node

        length = 0

        while current != None:
            length += 1
            current = current.next_element

        return length

    def insert_at_head(self, val):
        """
        O(1) time complexity
        O(1) space complexity
        """
        if self.head_node == None:
            self.head_node = Node(val)
            return "Inserted node at head"
        else:
            current = self.head_node
            self.head_node = Node(val)
            self.head_node.next_element = current
            del current
            return "Inserted node at head"

    def insert_at_tail(self, val):
        """
        O(n) time complexity
        O(1) space complexity
        """
        if self.head_node == None:
            self.head_node = Node(val)
        else:
            current = self.head_node
            while current.next_element != None:
                current = current.next_element

            current.next_element = Node(val)

        return "Inserted node at end"

    def search_element(self, val):
        """
        O(n) time complexity
        O(1) space complexity
        """
        current = self.head_node
        while current:
            if current.data == val:
                return True
            current = current.next_element

        return False

    def delete_at_head(self):
        """
        O(1) time complexity
        O(1) space complexity
        """
        current = self.head_node

        if current != None:
            new_head = current.next_element
            self.head_node = new_head
            del current

        return

    def delete_by_value(self, val):
        """
        O(n) time complexity
        O(1) space complexity
        """
        if self.head_node == None:
            return False

        if self.head_node.data == val:
            next_node = self.head_node.next_element
            if next_node:
                self.head_node.data = next_node.data
                self.head_node.next_element = next_node.next_element
        else:
            previous = self.head_node
            current = self.head_node.next_element
            while current:
                if current.data == val:
                    previous.next_element = current.next_element
                    del current
                    return True
                previous = current
                current = current.next_element

        return False

    def reverse_list(self):
        """
        O(n) time complexity
        O(1) space complexity
        """

        previous = None
        current = self.head_node
        next_node = None

        while current:
            next_node = current.next_element
            current.next_element = previous
            previous = current
            current = next_node

        lst.head_node = previous

        return lst

    def find_mid(self):
        """
        O(n) time complexity
        O(1) space complexity
        """

        if self.head_node == None:
            return False

        length = self.__len__()

        if length % 2 == 0:
            mid = length // 2
        else:
            mid = length // 2 + 1

        index = 1
        current = self.head_node
        while mid > index:
            current = current.next_element
            index += 1

        return current.data

    def find_mid_two_pointers(self):
        """
        O(n) time complexity
        O(1) space complexity
        """

        if self.head_node == None:
            return False

        current = self.head_node

        if current.next_element == None:
            return current.data

        mid = current
        current = current.next_element.next_element

        while current:
            mid = mid.next_element
            current = current.next_element
            if current:
                current = current.next_element
        if mid:
            return mid.data
        return False

    def remove_duplicates(self):
        seen_nodes = {}

        if self.head_node == None:
            return False

        previous = self.head_node
        current = previous.next_element

        while current:
            if seen_nodes.get(current.data):
                next_node = current.next_element
                previous.next_element = next_node
                current = next_node
            else:
                seen_nodes[current.data] = True
                current = current.next_element

        return

    def union_lists(self, other_list):

        # get all nodes in list1 (hash table)
        # append nodes from list2 that don't exist in list1
        pass

    def intersection_lists(self, other_list):

        # get all nodes in list1 (hash table)
        # return list of nodes only present in both
        pass

    def find_nth(self):

        # traverse through list till length + 1 - n
        # return nth value from end
        pass