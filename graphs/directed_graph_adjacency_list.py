from linked_lists.singly_linked_list import Node, SinglyLinkedList
from queues.queue import Queue

class Graph:

    def __init__(self, number_of_nodes):
        # total number of nodes in graph
        self.number_of_nodes = number_of_nodes
        # defining a list which can hold multiple SinglyLinkedLists
        # equal to number of nodes in the graph
        self.array = []
        # creating a new SinglyLinkedList for each node of the list (by index)
        for _ in range(self.number_of_nodes):
            temp = SinglyLinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        """Add an edge from source to destination
        O(1) time complexity
        O(1) space complexity
        """

        if (source < self.number_of_nodes and destination < self.number_of_nodes):
            self.array[source].insert_at_head(destination)
            # for an UNDIRECTED GRAPH, you would do the same for the destination node
            # self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print("\n")
        for i in range(self.nodes):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")

    def bfs_traversal(self, source):
        """
        O(n + e) time complexity
        O(n) space complexity
        """

        result = ""
        num_of_nodes = self.number_of_nodes

        if num_of_nodes == 0:
            return result

        queue = Queue()
        queue.enqueue(source)

        while not queue.is_empty():
            current_node = queue.dequeue()
            result = result + str(current_node)

            edges = self.array[current_node]

            if edges == None:
                continue

            current_edge = edges.get_head()

            while current_edge:
                queue.enqueue(current_edge.data)
                current_edge = current_edge.next_element

        return result
