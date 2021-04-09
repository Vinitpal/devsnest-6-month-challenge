# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data # Assign data
        self.next = next # Initialize next as null
    
# Linked List class
class LinkedList:
    # Function to initialize the list object
    def __init__(self):
        self.head = None


    # Function to print Linked List 
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next


    # Function to insert new node at the beginning
    def insert_at_start(self, new_data):
        # Allocate the Node and put in the data
        new_node = Node(new_data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node


    # Function to insert after given prev_node
    def insert_after(self, prev_node, new_data):
        # check if prev_node exists or not
        if prev_node is None:
            print("The given previous node is not in linkedList")
            return
        
        # create new node and put it in the data
        new_node = Node(new_data)

        # Make next of new node as next of prev_node
        # i.e. if it was 3 --> 4 and we add 2 in middle
        # so this line will do this 2 --> 4 
        new_node.next = prev_node.next

        # Make next of prev_node as new_node
        # This line will connect 3 and 2 like
        # 3 --> 2 --> 4
        prev_node.next = new_node


    # Function to insert new_node at the end
    def insert_at_end(self, new_data):
        # Create a new_node and put it in data
        new_node = Node(new_data)

        # If linkedList is empty then make the new_node as head
        if self.head is None:
            self.head = new_node
            return
        # Else traverse till last node
        last = self.head
        while(last.next):
            last = last.next # This is like incrementing
        
        # Finally change the next of last_node
        last.next = new_node



# A simple Python program to introduce a linked list
if __name__=='__main__':
    # start with the empty list
    llist = LinkedList()

    llist.head = Node("Dio")
    second = Node("Jojo")
    third = Node("Kirua")

    llist.head.next = second
    second.next = third

    llist.printList()