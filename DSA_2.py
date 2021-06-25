class Node:
     
    def __init__(self, data):
         
        self.data = data
        self.left = None
        self.right = None
         
# Structure to store node pair onto stack
class snode:
     
    def __init__(self, l, r):
         
        self.l = l
        self.r = r
  
''' Helper function that allocates a new node with the
given data and None left and right pointers. '''
def newNode(data):
 
    new_node = Node(data)
    return new_node
     
''' Given a binary tree, print its nodes in inorder'''
def inorder(node):
 
    if (not node):
        return;
  
    ''' first recur on left child '''
    inorder(node.left);
  
    ''' then print the data of node '''
    print(node.data, end=' ');
  
    ''' now recur on right child '''
    inorder(node.right);
  
''' Function to merge given two binary trees'''
  
def MergeTrees(t1, t2):
 
    if (not t1):
        return t2;
    if (not t2):
        return t1;
    s = []
     
    temp = snode(t1, t2)
     
    s.append(temp);
    n = None
     
    while (len(s) != 0):
     
        n = s[-1]
        s.pop();
         
        if (n.l == None or n.r == None):
            continue;
             
        n.l.data += n.r.data;
        if (n.l.left == None):
            n.l.left = n.r.left;
        else:
            t=snode(n.l.left, n.r.left)
            s.append(t);
         
        if (n.l.right == None):
            n.l.right = n.r.right;
        else:
 
            t=snode(n.l.right, n.r.right)
            s.append(t);
         
    return t1;
  
# Driver code
if __name__=='__main__':
     
    ''' Let us construct the first Binary Tree
            1
          /   \
         2     3
        / \     \
       4   5     6
    '''
   
    root1 = newNode(1);
    root1.left = newNode(2);
    root1.right = newNode(3);
    root1.left.left = newNode(4);
    root1.left.right = newNode(5);
    root1.right.right = newNode(6);
   
         
    root2 = newNode(4);
    root2.left = newNode(1);
    root2.right = newNode(7);
    root2.left.left = newNode(3);
    root2.right.left = newNode(2);
    root2.right.right = newNode(6);
   
    root3 = MergeTrees(root1, root2);
    print("The Merged Binary Tree is:");
    inorder(root3)