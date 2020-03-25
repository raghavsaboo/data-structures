# Trees 🌲

## Definition
An abstract data type that sores elements hierarchically. Each element (except the top element) has a **parent** element and zero or more **children** elements. 

## Key properties
- `Root` - node with no parent
- `Parent` -  an immediate ancestor of node
- `children` - descendents of a node
- `depth` - the number of ancestors of a node, excluding itself
  - if node `n` is the root, then the depth of `n` is 0
  - otherwise, the depth of `n` is `1 + depth of the parent of n`
- `height` - the number of descendents of a node, excluding itself
  - if node `n` is a leaf, then the height of `n` is 0
  - otherwise, the height of `n` is `1 + max(heights of n's children)`

## Binary Trees

### Definition
A **binary tree** is an ordered tree with the following properties:
- Every node has at most two children
- Each child node is labeled as being either a *left child* or a *right child*
- A left child precedes a right child in the order of children of a node.

### Key Properties
- `left subtree` - subtree rooted at a left child of an internal node n
- `right subtree` - subtree rooted at a right child of an internal node n