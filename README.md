# Data Structures in General

## Linear Data Structures

In linear data structures, each element is connected to either one (the next element) or two (the next and previous) more elements. Traversal in these structures is linear, meaning that insertion, deletion, and search work in `O(n)`.

Lists, linked lists, stacks, and queues are all example of linear data structures.

## Non-Linear Data Structures

The exact opposite of linear data structures is non-linear data structures. In a non-linear data structure, each element can be connected to several other data elements. Traversal is not linear and, hence, search, insertion, and deletion can work in `O(log n)` and even `O(1)` time.

Trees, graphs and hash tables are all non-linear data structures.

## Overview and Key Points

| Data Structure      | Key Points                                                                                                                                                                                                                                                                                    |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primitive Types     | Know how `int`, `char`, `double` etc. are represented in memory and the primitive operations on them                                                                                                                                                                                          |
| Arrays              | Fast access for elements at an index, slow lookups (unless sorted) and insertions. Be comfortable with notions of iteration, resizing, partitioning, merging, etc.                                                                                                                            |
| Strings             | Know how strings are represented in memory. Understand basic operators such as comparison, copying, matching, joining, splitting, etc.                                                                                                                                                        |
| Lists               | Understand trade-offs with respect to arrays. Be comfortable with iteration, insertion, and deletion within singly and doubly linked lists. Know how to implement a list with dynamic allocation, and with arrays.                                                                            |
| Stacks and Queues   | Recognize where Last-in First-out (stack) and First-in First-out (queue) semantics are applicable. Know array and linked list implementations.                                                                                                                                                |
| Binary trees        | Use for representing hierarchical data. Know about depth, height, leaves, search path, traversal sequences, successor/predecessor operations.                                                                                                                                                 |
| Heaps               | Key benefit: `O(1)` lookup find-max `O(log n)` insertion, and `O(log n)` deletion of max. Node and array representations. Min-heap variant.                                                                                                                                                   |
| Hash tables         | Key benefit: `O(1)` insertions, deletions, and lookups. Key disadvantages: not suitable for order-related queries; need for resizing; poor worst-case performance. Understand implementation using array of buckets and collision chains. Know hash functions for integers, strings, objects. |
| Binary search trees | Key benefit: `O(log n)` insertions, deletions, lookups, find-max, find-min, successor, predecessor when tree is height-balanced. Understand node fields, pointer implementation. Be familiar with notion of balance, and operations maintaining balance.                                      |

## Time and Space Complexity Cheat Table

|                    Data Structure                     |              Insert              |              Delete              |              Search              |         Space complexity         |
| :---------------------------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: |
|                         Array                         |               O(n)               |               O(n)               |               O(n)               |               O(n)               |
|                  Single linked list                   |      O(1) (insert at head)       |        O(1) (delete head)        |               O(n)               |               O(n)               |
|                  Doubly linked list                   |      O(1) (insert at head)       |        O(1) (delete head)        |               O(n)               |               O(n)               |
|        Doubly linked list (with tail pointer)         |  O(1) (insert at head or tail)   |    O(1) (delete head or tail)    |               O(n)               |               O(n)               |
|                         Stack                         |           O(1) (push)            |            O(1) (pop)            |               O(n)               |               O(n)               |
|                         Queue                         |          O(1) (enqueue)          |          O(1) (dequeue)          |               O(n)               |               O(n)               |
|                      Binary heap                      |             O(lg n)              |      O(lg n) (removeMin())       |               O(n)               |               O(n)               |
|                      Binary tree                      |               O(n)               |               O(n)               |               O(n)               |               O(n)               |
|                  Binary search tree                   |               O(n)               |               O(n)               |               O(n)               |               O(n)               |
|              Red-Black / AVL / 2-3 Tree               |             O(lg n)              |             O(lg n)              |             O(lg n)              |               O(n)               |
|                      Hash table                       | O(n): worst case O(1): amortized | O(n): worst case O(1): amortized | O(n): worst case O(1): amortized | O(n): worst case O(1): amortized |
| Trie (size of alphabet: d, length of longest word: n) |               O(n)               |               O(n)               |               O(n)               |              O(d^n)              |

## Graph Operations Complexities

Time complexities of some common operations in a graph with n vertices and m edges.

|          Operation           | Adjacency list | Adjacency matrix |
| :--------------------------: | :------------: | :--------------: |
|          Add vertex          |      O(1)      |       O(1)       |
|        Remove vertex         |     O(m+n)     |      O(n^2)      |
|           Add edge           |      O(1)      |       O(1)       |
|         Remove edge          |      O(n)      |       O(1)       |
| Depth / Breadth first search |     O(m+n)     |      O(n^2)      |
|       Space complexity       |     O(m+n)     |      O(n^2)      |