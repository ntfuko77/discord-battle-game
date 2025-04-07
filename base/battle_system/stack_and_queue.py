class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class base_stack:
    def __init__(self):
        self.top = None
        self.size=0
    def push(self, data):
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node
        self.size+=1
    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size-=1
        return data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
class base_queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size=0
    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size+=1
    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size-=1
        return data
        
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
    def is_empty(self):
        return self.front is None

class stack(base_stack):
    def __init__(self):
        super().__init__()
    def insert(self,data):
        buffer=self.pop()
        self.push(data)
        self.push(buffer)

class queue(base_queue):
    def __init__(self):
        super().__init__()
    def enqueue(self,data:str)
    def fetchall(self)->str:
        buffer=''
        while not self.is_empty():
            current = self.enqueue
            buffer+=current.data+'\n'
            return buffer
        
        
        
