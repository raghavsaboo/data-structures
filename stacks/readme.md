# Stacks

## Definition
A collection of objects that are inserted (push) and removed (pop) according to the **LAST IN, FIRST OUT (LIFO)** semantics.

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
        <td>O(n)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Search</td>
        <td>O(n)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Insertion</td>
        <td>O(1)</td>
        <td>O(1)</td>
    <tr>
        <td>Deletion</td>
        <td>O(1)</td>
        <td>O(1)</td>
    </tr>
</table>

**Spacy Complexity (Worst)** - O(n)

## Top Tips

- Learn to recognize when the stack's **LIFO** property is  _applicable_.
  - e.g. when parsing, or addresses of recently visited sites, or "undo" mechanism, or function call stacks
- Consider **augmenting** the basic stack or queue data structure to support additional operations, such as finding the maximum element.

# Implemetations
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

*Due to **amortized** bounds of Python `list`, a typical call to either of these methods uses constant time, but there is occosionally an O(n) time worst case when an operation causes the list to resize it's internal array.*

Space usage is still O(n).

## Avoiding Amortization by Reserving Capacity
### `array_stack_preallocated.py`

#### Motivation
- Some contexts may provide additional knowledge that suggests a maximum size that a stack will reach.
- It is also more efficient in practice to construct a list with initial length `n` than it is to start with an empty list and append `n` items (even though both approaches run in O(n) time).


#### Modifications
- Constructor accepts a parameter specifying the maximum capacity of a stack and initializes it to that length.
- Size of the stack would no longer be synonymous with the length of the list - a sepearte integer would be used to denote the current number of elements in the stack.

# Example Use Cases

## Reverse Data Using a Stack
### `reverse_file.py`

We wish to print lines of a file in reverse order in to display a data set in decreasing order rather than increasing order.

## Test a string over `"{,},(,),[,]"` for well-formedness.
### `well_formed_string.py`

A string over the characters `"{,},(,),[,]"` is said to be well-formed if the different types of brackets match in the correct order.

This program tests if a string made up of the characters are well formed.