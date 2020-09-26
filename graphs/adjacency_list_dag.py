from linked_lists.singly_linked_list import Node, SinglyLinkedList
from queues.custom_queue import CustomQueue
from stacks.stack import Stack

class AdjacencyListDAG:

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
        for i in range(self.number_of_nodes):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")
            
    def _bfs_traversal_helper(self, source, visited):
        result = ""
        # Create Queue for BFS Traversal and enqueue source in it
        queue = CustomQueue()
        queue.enqueue(source)
        # Mark as visited
        visited[source] = True
        # Traverse while queue is not empty
        while not queue.is_empty():
            # Dequeue a node from the queue and add it to the result
            current_node = queue.dequeue()
            result += str(current_node)
            # Get adjacent vertices to the current_node from the list,
            # and if they are not already visited then enqueue them in 
            # the Queue
            temp = self.array[current_node].head_node
            
            while temp != None:
                if visited[temp.data] == False:
                    queue.enqueue(temp.data)
                    # Mark as visited
                    visited[temp.data] = True
                temp = temp.next_element
        return result, visited
        
        
    def bfs_traversal(self, source):
        """
        O(n + e) time complexity
        O(n) space complexity
        """

        result = ""
        num_nodes = self.number_of_nodes

        if num_nodes == 0:
            return result
            
        # A list to hold the history of visited nodes
        # Make a node visited whenever you enqueue it into queue
        visited = []
        for _ in range(num_nodes):
            visited.append(False)
            
        # Start from the source
        result, visited = self._bfs_traversal_helper(source, visited)
         
        # Visit remaining nodes
        for node in range(num_nodes):
            if visited[node] == False:
                result_new, visited = self._bfs_traversal_helper(node, visited)
                result += result_new
                
        return result
        
    def _dfs_traversal_helper(self, source, visited):
        result = ""
        # Create Stack(Implemented in previous lesson) for Depth First Traversal
        # and Push source in it
        stack = Stack()
        stack.push(source)
        visited[source] = True
        # Traverse while stack is not empty
        while not stack.is_empty():
            # Pop a vertex/node from stack and add it to the result
            current_node = stack.pop()
            result += str(current_node)
            # Get adjacent vertices to the current_node from the array,
            # and if they are not already visited then push them in the stack
            temp = self.array[current_node].head_node
            while temp != None:
                if visited[temp.data] == False:
                    stack.push(temp.data)
                    # Visit the node
                    visited[temp.data] = True
                temp = temp.next_element
        return result, visited  # For the above graph it should return "12453"

    def dfs_traversal(self, source):
        """
        O(n + e) time complexity
        O(n) space complexity
        """
        result = ""
        num_nodes = self.number_of_nodes
        if num_nodes == 0:
            return result
        # A list to hold the history of visited nodes
        # Make a node visited whenever you push it into stack
        visited = []
        for _ in range(num_nodes):
            visited.append(False)
        # Start from source
        result, visited = self._dfs_traversal_helper(source, visited)
        # visit remaining nodes
        for node in range(num_nodes):
            if visited[node] is False:
                result_new, visited = self._dfs_traversal_helper(node, visited)
                result += result_new
        return result