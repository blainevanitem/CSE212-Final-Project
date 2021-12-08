# Python Queues



![Queue](images/queue_example.png)
## What is a Python Queue?
<font size=3>In python, a queue is a data structure following the common practice of "FIFO". This is otherwise known as "First in, First Out". The benefit of using the "FIFO" method is it provides everyone a fair opportunity to access something. In real like this would be like people waiting in line for a cashier. It allows everyone to gain access to the cashier, give the cashier their groceries and get checked out. 

The common terms for this data structure are Enqueue and Dequeue. Enqueue is when we place a new item into the queue, or if someone joins the end of the line in a checkout line. Dequeue is the opposite where the item that is oldest or at the first spot in the queue is taken off.

The python queue follows this same idea. One example would be when a website has a high volume of requests and is throttling the connection of the visitors. To be fair, it will allow those who joined first to be allowed access into the website at the earliest possible time and retrieve the data that they requested.

## Some example code:
```python
    def main():
        my_queue = [] # This is a list or queue.

        my_queue = put_on_queue(my_queue) # Call to the put on queue function to place a value onto the queue.

        my_queue = take_off_queue(my_queue) # Call to the take off queue function to remove the first item on the queue.
```
```python
    def put_on_queue(my_queue):
        value = _ # A value that you want to place onto the queue.

        my_queue.append(value) # This will place the value on the end of the queue.
    
        return my_queue
```
```python
    def take_off_queue(my_queue):
        my_queue.pop(0) # This will remove the first item in the queue.

        return my_queue
```

## Python Queue Performance
The performance of the different functions associated with python queues are as follows: 

            .append(value) - This places a value at the end of a python queue/list.
                Performance = O(1)
                
            .pop(0) - This will remove the first item in the queue, following the "FIFO" pattern.
                Performance = O(n)

            len(my_queue) - This will give us the total amount of items in a queue/list. You can also check if the queue is empty by seeing if the length equals zero.
                Performance = O(1)
            



## Now for practice!
The best way to learn is to code it yourself. For the problem you will have 10 customers that are getting in line(enqueue) to checkout at the grocery store. You have to make sure that all of them scan their items and are then checked out(dequeued) from the checkout line. Make sure to print out the items that each customer has the cashier ring out.

After working through it you can compare your solution to the file here: [Queue Python Solution](1-queue.py)



<!-- 
You should have an example problem that you propose and then help the student walk through to the solution.
You should also have a problem that the student solves (with a link to your solution). It looks like your example problem file is empty at this point. -->
