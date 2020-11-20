class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0) # Linked list object only has reference to the head node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
            
        current = self.head
        
        for _ in range(index + 1):
            current = current.next
        
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # can't add to an index that's more than the length
        if index > self.size:
            return
        
        # if index less than 0 do nothing 
        if index < 0:
            return
            
        # increase size of list
        self.size += 1
            
        # find the previous node
        previous_node = self.head
        for _ in range(index):
            previous_node = previous_node.next
            print(_)
            
        new_node = Node(val)
        
        new_node.next = previous_node.next
        previous_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        
        previous_node = self.head
        for _ in range(index):
            previous_node = previous_node.next
            
        previous_node.next = previous_node.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
val = 5
index = 0
obj.addAtIndex(index, val)
obj.get(0) #?
obj.addAtHead(7)
obj.get(0) #?
obj.addAtTail(8)
obj.get(2) #?
obj.deleteAtIndex(1)
obj.get(0) #?
obj.get(1) #?

# obj.deleteAtIndex(index)

