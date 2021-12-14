# Binary Trees
## What is a binary tree in python?

<font size=3>In Python, a tree is another example of a linked list but can be linked to different nodes extending from it using pointers. Although similar to linked lists,but in contrast they are able to link to multiple other nodes.

## Binary Tree
A binary tree is a tree that cannot connect to more than two nodes. Each "head" or root node extend to two or one nodes, also known are leaf nodes, and the way that we place data into the tree does not follow any set rules.

## Binary Search Tree
A binary search tree follows the same pattern as normal trees, but they follow set data rules. The rules that it follows are when it is placing data into the tree it checks whether the data being insert is lower or higher than its root and appropriately places it on the left(lower) or right(higher). Balanced Binary Search trees are a kind of tree that follows the data ruled as stated above and also is not unbalanced. When we say unbalanced, the tree looks lopsided and one child branch from the root is longer than the other.

An example of a real world world example would be family tree. If we assign ids to different family members in order of age we can successfully place them in the correct order into a tree.

As you can see it follows the same pattern of using nodes and linking them together.
```python
    class BST:
        class Node:
            def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None

        def __init__(self):
            self.root = None

```
How to insert into a tree:
```python
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

```
### The performance of the different functions associated with python trees are as follows: 

        Insert(Value) Insert into a tree. Go through the tree recursively until you find the correct place.
            Performance = O(log n)

        Remove(Value) Remove a node/value from a tree. Go through the tree recursively until you find the value you want to remove.
            Performance = O(log n)

        Contains(value)	Will tell us if the tree contains a certain value.
            Performance = O(log n)


![Linked List](images/binary_search_tree.png)

## What is recursion?
Recursion is the process of continuously calling a function over and over again until a condition, also known as a base case is met. We just have to make sure to yield anything we want to retrieve back from recursively called functions.

## Now for practice!
The problem you need to solve is creating a binary search tree that places numbers in their appropriate order, following the rules that lesser values go to the left leafs and the higher values go to the right leafs.

After working through it you can compare your solution to the file here: [Trees Python Solution](3-trees.py)
