import random

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = str(data)
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = LinkedList.Node(value)  
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node      
            
    def insert_tail(self, value):
        new_node = LinkedList.Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        linkedliststr = "linkedlist [ "
        curr = self.head
        while curr is not None:
            linkedliststr += str(curr.data) + " "
            curr = curr.next
        linkedliststr += "]"
        return linkedliststr


customers = LinkedList()
customers.insert_tail("Mark")
customers.insert_tail("Mary")
customers.insert_tail("Blaine")
customers.insert_tail("Rose")
customers.insert_tail("Sarah")
customers.insert_tail("Tony")
customers.insert_tail("Bob")
print(f'\nCustomers that are in the checklist:\n\n{customers}\n')

