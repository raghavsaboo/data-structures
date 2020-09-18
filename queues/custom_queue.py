class CustomQueue:

    def __init__(self):
        # Here we have implemented queue using python list.
        # However, if the queue is implemented using a Linked list,
        # the time complexity can be optimized to O(1).
        self.queue_list = []
        
    def size(self):
        return len(self.queue_list)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        front = self.front()
        self.queue_list.remove(self.front())
        return front