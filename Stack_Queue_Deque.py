#Implementing a Stack

class Stack(object):
    
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
##################################################################################################################
    
#Implementing a Queue

class Queue(object):
    
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
#################################################################################################################

#Implementing a Deque

class Deque(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items==[]
    
    def addFront(self,item):
        self.items.append(item)
        
    def addRear (self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

    
    
