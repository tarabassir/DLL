class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def search(self,data):
        node=self.head
        while node!=None and node.data!=data:
            node=node.next
        return node

    def insert(self,node):
        node.next=self.head
        if self.head!=None:
            self.head.prev=node
        self.head=node
        node.prev=None
        return

    def delete(self,node):
        if node.prev!=None:
            node.prev.next=node.next
        else:
            self.head=node.next
        if node.next!=None:
            node.next.prev=node.prev
        return
    def print_list(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
        return

    
