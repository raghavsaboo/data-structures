# Data Structures in General

| Data Structure | Key Points |
|----------------|------------|
| Primitive Types | Know how `int`, `char`, `double` etc. are represented in memory and the primitive operations on them |
| Arrays | Fast access for elements at an index, slow lookups (unless sorted) and insertions. Be comfortable with notions of iteration, resizing, partitioning, merging, etc. |
| Strings | Know how strings are represented in memory. Understand basic operators such as comparison, copying, matching, joining, splitting, etc. |
| Lists | Understand trade-offs with respect to arrays. Be comfortable with iteration, insertion, and deletion within singly and doubly linked lists. Know how to implement a list with dynamic allocation, and with arrays. |
| Stacks and Queues | Recognize where Last-in First-out (stack) and First-in First-out (queue) semantics are applicable. Know array and linked list implementations. |
| Binary trees | Use for representing hierarchical data. Know about depth, height, leaves, search path, traversal sequences, successor/predecessor operations. |
| Heaps | Key benefit: `O(1)` lookup find-max `O(log n)` insertion, and `O(log n)` deletion of max. Node and array representations. Min-heap variant. |
| Hash tables | Key benefit: `O(1)` insertions, deletions, and lookups. Key disadvantages: not suitable for order-related queries; need for resizing; poor worst-case performance. Understand implementation using array of buckets and collision chains. Know hash functions for integers, strings, objects. |
| Binary search trees | Key benefit: `O(log n)` insertions, deletions, lookups, find-max, find-min, successor, predecessor when tree is height-balanced. Understand node fields, pointer implementation. Be familiar with notion of balance, and operations maintaining balance. |