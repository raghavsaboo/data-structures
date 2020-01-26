# Arrays


## Definition
The simplest data structure is the array, which is a contiguous block of memory, usually used to represent sequences.

## Complexity

<table>
    <tr>
        <th>Method</th>
        <th colspan=2>Time Complexity</th>
    </tr>
    <tr>
        <td colspan=1></td>
        <td colspan=1>Average</td>
        <td colspan=1>Worst </td>
    </tr>
    <tr>
        <td>Access</td>
        <td>O(1)</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>Search</td>
        <td>O(n)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Insertion</td>
        <td>O(n)</td>
        <td>O(n)</td>
    <tr>
        <td>Deletion</td>
        <td>O(n)</td>
        <td>O(n)</td>
    </tr>
</table>

**Space Complexity (Worst)** - O(n)

## Top Tips
- When working with arrays you should take advantage of the fact that you can operate efficiently on both ends. e.g. if you have an array of integers and you want events to appear first, you can partition the array into three sub-arrays: Even, Unclassified, and Odd. Iterating through the array you can move elements to the boundaries of the Even and Odd sub-arrays through swaps.
- Array problems often have simple brute-force solutions that use `O(n)` space, but there are subtler solutions that **use the array itself** to **reduce space** complexity to `O(1)`.
- Filling an array from the front is slow, so see if it is possible to **write balues from the back**.
- Instead of deleting an entry (which requires moving all entries to its right), consider **overwriting** it.
- 

# Implementations
## Base Implementation - Adapt Python `list` to Implement Stack
### `array_stack.py`

We can implement a stack quite easily by storing its elements in a Python `list`.
- The list class already supports adding an element to the end with the `append` method, and removing the last element with the `pop` method.
- So we can use the **Adapter** pattern:
  - modify an existing class so that its methods match those of a related, but different class or interface
  - general way to apply the adapter pattern is to define a new class such that it contains an instance of the existing class as a hidden field, and then to implement each method of the new class using methods of this hidden instance variable.

<table>
    <tr>
        <th>Stack Method</th>
        <th>Python <code>list</code> Method</th>
    </tr>
    <tr>
        <td><code>stack.pop(e)</code></td>
        <td><code>list.pop(e)</code></td>
    </tr>
    <tr>
        <td><code>stack.top()</code></td>
        <td><code>list[-1]</code></td>
    </tr>
    <tr>
        <td><code>stack.is_empty()</code></td>
        <td><code>len(list) == 0</code></td>
    </tr>
    <tr>
        <td><code>len(stack)</code></td>
        <td><code>len(list)</code></td>
    </tr>
</table>

*Due to **amortized** bounds of Python `list`, a typical call to either of these methods uses constant time, but there is occasionally an O(n) time worst case when an operation causes the list to resize it's internal array.*

Space usage is still O(n).

## Avoiding Amortization by Reserving Capacity
### `array_stack_preallocated.py`

#### Motivation
- Some contexts may provide additional knowledge that suggests a maximum size that a stack will reach.
- It is also more efficient in practice to construct a list with initial length `n` than it is to start with an empty list and append `n` items (even though both approaches run in O(n) time).

#### Modifications
- Constructor accepts a parameter specifying the maximum capacity of a stack and initializes it to that length.
- Size of the stack would no longer be synonymous with the length of the list - a separate integer would be used to denote the current number of elements in the stack.

## Getting Max Element from a Stack
### `array_stack_with_cached_max.py`

#### Motivation
- Build in a store of maximum in the stack at any given moment without requiring to iterate through the whole stack every time it is updated

#### Modifications
- The time complexity for iterating through the underlying array for an array-based stack is O(n) and the space complexity is O(1)
- The time complexity can be reduced to O(log n) using auxiliary data structures e.g. heap or BST and a hash table. The space complexity increases to O(n) and the code complexity is high
- So instead we could use a single auxiliary variable M to record the element that is maximum in the stack
  - Updating M is easy on pushes: M = max(M, e)
  - However updating M on pop is very time consuming (have to iterate through the stack to find the new max again)
- INSTEAD we can **cache** for each element, the max at the **time of push**
  - Specifically for each entry in the stack, we cache the maximum stored at or below that entry
  - Now when we pop, we evict the corresponding cached value

# Example Use Cases

## Reverse Data Using a Stack
### `reverse_file.py`

We wish to print lines of a file in reverse order in to display a data set in decreasing order rather than increasing order.

## Test a string over `"{,},(,),[,]"` for well-formedness.
### `well_formed_string.py`

A string over the characters `"{,},(,),[,]"` is said to be well-formed if the different types of brackets match in the correct order.

This program tests if a string made up of the characters are well formed.
