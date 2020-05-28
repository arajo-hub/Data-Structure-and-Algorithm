# Queue

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, data):
        # Queue가 비어있을 때
        if self.tail is None:
            self.head=self.tail=Node(data)
        # Queue가 비어있지 않을 때
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next

    def dequeue(self):
        # Queue가 비어있을 때
        if self.head is None:
            return None
        # Queue가 비어있지 않을 때
        else:
            dequeue_data=self.head.data
            self.head=self.head.next
            return dequeue_data