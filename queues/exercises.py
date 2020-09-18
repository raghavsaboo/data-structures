from queues.custom_queue import CustomQueue
from stacks.stack import Stack

"""
Problem Statement
-----------------
Implement a function find_bin(n) which will generate binary numbers
from 1 till n in the form of a string using a queue.

# Input
A positive integer n

# Output
Returns binary numbers in the form of strings from 1 up to n

# Sample Input
>> n = 3

# Sample Output
>> result = ["1","10","11"]

# Sample Input
>> n = 5

# Sample Output
>> result = ["1", "10", "11", "100", "101"]
"""


def find_bin(n):
    """
    O(n) time complexity
    O(n) space complexity
    """
    result = []
    queue = CustomQueue()

    queue.enqueue(1)

    for i in range(n):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result


print(find_bin(3))
print(find_bin(5))

"""
Problem Statement
-----------------
Implement the function reverse_k(queue, k) which takes a queue and a number “k” 
as input and reverses the first “k” elements of the queue. An illustration is 
also provided for your understanding.

# Output
The queue with first “k” elements reversed. Remember to return the queue itself!

# Sample Input
>> Queue = [1,2,3,4,5,6,7,9,10], k = 5

# Sample Output
>> Queue = [5,4,3,2,1,6,7,8,9,10]
"""


def reverse_k(queue, k):
    """
    O(n) time complexity
    O(k) space complexity
    """
    if queue.is_empty() is True or k > queue.size() or k < 0:
        # Handling invalid input
        return None

    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())

    while stack.is_empty() is False:
        queue.enqueue(stack.pop())

    size = queue.size()

    for _ in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue


# testing our logic
queue = CustomQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print("the queue before reversing:")
print(queue.queue_list)
reverse_k(queue, 10)
print("the queue after reversing:")
print(queue.queue_list)
