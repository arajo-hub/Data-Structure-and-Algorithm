# Stack

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self, data):
        if self.head is None: # Stack이 비어있다면
            self.head=Node(data)
        else: # Stack이 비어있지 않다면
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node

    # Stack에서 빼주기
    def pop(self):
        if self.head is None: # Stack이 비어있다면
            return None
        else: # Stack이 비어있지 않다면
            popped=self.head.data
            self.head=self.head.next
            return popped

