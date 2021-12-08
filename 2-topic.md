# Linked Lists
## What is a linked list in python?

<font size=3>In Python, a linked list is a collection of data structures known as nodes. Where the term "linked list" comes from is how the different nodes are setup to be linked together. Each node contains a data value, a head, and a tail. The head of the node points to the node that was placed in front of it and if it is the first in the linked list is classified as the head of the linked list. Likewise, the tail is the last node in the linked list. 

Common functions for this data set are changing the head or tail, as well as removing a node from the linked list. When removing a node from a linked list you have to remove both the connection between the node before it and after it. Then you update the next and previous pointers.

A real world example of a practical use of this would be...
```python
    def hello():

```

A linked list is:
![Linked List](images/linked_list.jpeg)

For an example of a linked list in python code click here:
[Linked List Python Example](2-linked_list.py)

### The performance of the different functions associated with python queues are as follows: 

            insert/remove head or the tail(value) - Also known as appending to the beginning or the end of the linked list.
                Performance = O(1)
                
            insert(index, value) - This will loop through until it reaches the index that you want the value inserted.
                Performance = O(n)

            remove(value)) - This will loop through the linked list until it reaches the correct value and remove it from the linked list.
                Performance = O(n)

            size() - This will return how many nodes there are in the linked list.
                Performance = O(1)

            empty() - Will return true if there are no nodes in the linked list.
                Performance = O(1)



A double linked list is one that has both a next and previous pointer, rather than just a next pointer. 

![Double Linked List](images/linked_list_double.jpeg)

## Now for practice!
The best way to learn is to code it yourself. For the problem you will have to ...

After working through it you can compare your solution to the file here: [Linked List Python Solution](2-linked_list.py)

<!-- You should have an example problem that you propose and then help the student walk through to the solution.
You should also have a problem that the student solves (with a link to your solution). It looks like your example problem file is empty at this point. -->
