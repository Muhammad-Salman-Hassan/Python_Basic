
# Python3 program merge two sorted linked
# in third linked list using recursive.
 
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
# Constructor to initialize the node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Method to print linked list
    def printList(self):
        temp = self.head
         
        while temp :
            print(temp.data, end="->")
            temp = temp.next
 
    # Function to add of node at the end.
    def append(self, new_data):
        new_node = Node(new_data)
         
        if self.head is None:
            self.head = new_node
            return
        last = self.head
         
        while last.next:
            last = last.next
        last.next = new_node
    
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next = current
            current.next=prev
            prev=current
            current=next
        self.head=prev
 
# Function to merge two sorted linked list.
def mergeLists(head1, head2):
 
    # create a temp node NULL
    temp = None
 
    # List1 is empty then return List2
    if head1 is None:
        return head2
 
    # if List2 is empty then return List1
    if head2 is None:
        return head1
 
    # If List1's data is smaller or
    # equal to List2's data
    if head1.data <= head2.data:
 
        # assign temp to List1's data
        temp = head1
 
        # Again check List1's data is smaller or equal List2's 
        # data and call mergeLists function.
        temp.next = mergeLists(head1.next, head2)
         
    else:
        # If List2's data is greater than or equal List1's 
        # data assign temp to head2
        temp = head2
 
        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        temp.next = mergeLists(head1, head2.next)
 
    # return the temp list.
    return temp
 
 
# Driver Function
if __name__ == '__main__':
 
    # Create linked list :
    # 10->20->30->40->50
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    
    list1.append(4)
    
 
    # Create linked list 2 :
    # 5->15->18->35->60
    list2 = LinkedList()
    list2.append(1)
    list2.append(3)
    list2.append(4)
   
 
    # Create linked list 3
    list3 = LinkedList()
 
    # Merging linked list 1 and linked list 2
    # in linked list 3
    list3.head = mergeLists(list1.head, list2.head)
 
    print(" Merged Linked List is : ", end=" ")
    list3.printList()     
 

class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
            
        
 
 
# Driver code
llist = LinkedList()
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(7)
llist.push(8)
 
print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()    
