from graphs.adjacency_list_dag import AdjacencyListDAG
from stacks.stack import Stack

"""
Problem Statement
------------------

A cycle exists when you traverse the directed graph and come upon a node that 
has already been visited.

You have to implement the detect_cycle function which tells you whether or not a graph contains a cycle.

# Input
A directed graph.

# Output
True if a cycle exists. False if it doesn’t.

# Tests
g1 = AdjacencyListDAG(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(3, 0)
g2 = AdjacencyListDAG(3)
g2.add_edge(0, 1)
g2.add_edge(1, 2)

print(detect_cycle(g1) == True)
print(detect_cycle(g2) == False)
"""


def detect_cycle(g):
    """
    Time Complexity: O(V+E)
    """
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.number_of_nodes

    # rec_node_stack keeps track of the nodes which are part of the
    # current recursive call
    rec_node_stack = [False] * g.number_of_nodes

    for node in range(g.number_of_nodes):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True

    return False


def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if (rec_node_stack[node]):
        return True

    # It has been visited before this recursion
    if (visited[node]):
        return False

    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True

    head_node = g.array[node].head_node
    while (head_node is not None):
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        if (detect_cycle_rec(g, adjacent, visited, rec_node_stack)):
            return True
        head_node = head_node.next_element

    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False


"""
Problem Statement
-----------------
You have to implement the find_mother_node() function which will 
take a directed graph as an input and find out which node is the mother 
node in the graph.

By definition, the mother node is one from which all other nodes are 
reachable. A graph can have multiple mother nodes, but you only need to 
find one.

# Input
A directed graph

# Output
Returns the value of the mother node if it exists. Otherwise, it returns -1

# Tests
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 0)
g.add_edge(3, 1)
print(find_mother_node(g))
"""

# Naive Solution

def find_mother_node_solution_one(g):
    """
    Time Complexity O(V(V+E))
    """
    # Performs DFS Traversal on graph starting from source
    # Returns total number of nodes which can be reached from source
    def perform_dfs(g, source):
        number_of_nodes = g.number_of_nodes
        nodes_reached = 0  # To store how many nodes reached from source
        # A list to hold the history of visited nodes (by default all false)
        # Make a node visited whenever you push it into stack
        visited = [False] * number_of_nodes

        # Create Stack (Implemented in previous section) for Depth First Traversal
        # and Push source in it
        stack = Stack()
        stack.push(source)
        visited[source] = True
        # Traverse while stack is not empty
        while (stack.is_empty() is False):
            # Pop a node from stack
            current_node = stack.pop()
            # Get adjacent nodes to the current_node from the list,
            # and if only push unvisited adjacent nodes into stack
            temp = g.array[current_node].head_node
            while (temp is not None):
                if (visited[temp.data] is False):
                    stack.push(temp.data)
                    visited[temp.data] = True
                    nodes_reached += 1
                temp = temp.next_element
            # end of while
        return nodes_reached + 1  # +1 is to include the source itself
    
    # Traverse the Graph Array and perform DFS operation on each node
    # The node whose DFS Traversal results is equal to the total number
    # of nodes in graph is a mother node
    num_of_nodes_reached = 0
    for i in range(g.number_of_nodes):
        num_of_nodes_reached = perform_dfs(g, i)
        if (num_of_nodes_reached is g.number_of_nodes):
            return i
    return - 1

# Last Finished Node Solution / Kosaraju's Strongly Connected Component Algorithm
def find_mother_node_solution_two(g):
    """
    Time Complexity O(V+E)
    The DFS of the whole graph works in O(V + E). If a mother vertex exists,
    the second DFS takes O(V + E) as well. Therefore, the complete time 
    complexity for this algorithm is O(V + E).
    """
    
    # A recursive function to print DFS starting from v
    def perform_dfs(g, node, visited):

        # Mark the current node as visited and print it
        visited[node] = True

        # Recur for all the nodes adjacent to this node
        temp = g.array[node].head_node
        while(temp):
            if visited[temp.data] is False:
                perform_dfs(g, temp.data, visited)
            temp = temp.next_element
    
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False]*(g.number_of_nodes)

    # To store last finished node (or mother node)
    last_v = 0

    # Do a DFS traversal and find the last finished
    # node
    for i in range(g.number_of_nodes):
        if visited[i] is False:
            perform_dfs(g, i, visited)
            last_v = i

    # If there exist mother node (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother node (or graph
    # has a mother node). We basically check if every node
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all nodes are
    # reachable from it or not.
    visited = [False]*(g.number_of_nodes)
    perform_dfs(g, last_v, visited)
    if any(i is False for i in visited):
        return -1
    else:
        return last_v

