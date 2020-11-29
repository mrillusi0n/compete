class Node:
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return 'Node: {}'.format(self.key)

class BinarySearchTree:

    def __init__(self):
        self.root = None 

    def find_in_order_successor(self, inputNode):
        currTraveller = self.root
        currKey = self.root.key
        currSuccessor = None
        
        key = inputNode.key

        while currTraveller:
            if currTraveller.key > key:
                if currTraveller.key <= currKey:
                    currSuccessor = currTraveller
                    currKey = currTraveller.key
                currTraveller = currTraveller.left
            else:
                currTraveller = currTraveller.right
                currKey = currTraveller.key if currTraveller else currKey

        
        return currSuccessor
        


    def insert(self, key):
        
        if (self.root is None):
            self.root = Node(key)
            return
                
        currentNode = self.root
        newNode = Node(key)
        while(currentNode is not None):
            
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.left;
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.right;

    def getNodeByKey(self, key):
        
        currentNode = self.root
        while(currentNode is not None):
            if(key == currentNode.key):
                return currentNode
                
            if(key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
                
        return None
                

bst     = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11); 
bst.insert(14);     

test = bst.getNodeByKey(12)

succ = bst.find_in_order_successor(test)

if succ is not None:
    print ("\nInorder Successor of %d is %d " \
                    %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")

