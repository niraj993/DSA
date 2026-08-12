class Node:
    def __init__(self,value:int):
        self.value = value
        self.next = None


 
class SinglyLinkedList:

    def __init__(self):
        self.head = None


    def append(self,value):
        new_node = Node(value=value)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traversal(self)->str:
        if self.head is None:
            print("singlyLinkedList is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value,end="")
                curr = curr.next
                print()

    def insert(self,value:int,pos:int):
        new_node = Node(value=value)
      



s1 = SinglyLinkedList()
s1.traversal()
s1.append(4)
s1.append(5)
s1.append(6)
s1.traversal()