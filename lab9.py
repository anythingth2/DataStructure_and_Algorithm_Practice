import random

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str({'data':self.data,'left':self.left,'right':self.right})


class BST:
    def __init__(self,data=None):
        self.root = Node(data)
        self.level = -1
    
    def _printSideway(root,level):
        if root != None and root.data != None:
            BST._printSideway(root.right,level+1)
            print(' '*(3*level),root.data)
            BST._printSideway(root.left,level+1)
    def printSideway(self):
        BST._printSideway(self.root,0)
    
    def insertR(root,data):
        if root.data == None:
            root.data = data
            return
        if data < root.data:
            if root.left != None:
                BST.insertR(root.left,data)
            else:
                root.left = Node(data)
        else:
            if root.right != None:
                BST.insertR(root.right,data)
            else:
                root.right = Node(data)
    def insertNode(root,node):
        if root.data == None:
            root.data = node
            return
        if node.data < root.data:
            if root.left != None:
                BST.insertNode(root.left,node)
            else:
                root.left = node
        else:
            if root.right != None:
                BST.insertNode(root.right,node)
            else:
                root.right = node
    def _inOrder(root,lamb=None):
        if root.left != None:
            BST._inOrder(root.left,lamb)
        if root.data != None:
            if lamb == None:
                print(root.data,end=' ')
            else:
                lamb(root.data)
        if root.right != None:
            BST._inOrder(root.right,lamb)
    def inOrder(self):
        BST._inOrder(self.root)
    def _search(root,data):
        ret = None
        if root.left != None:
            ret = BST._search(root.left,data)
        if root.data != None and ret == None:
            if root.data == data:
                ret = root
        if root.right != None and ret == None:
            ret = BST._search(root.right,data)
        return ret

    def search(self,data):
        return BST._search(self.root,data)
        
    def _path(root,data):
        if root.left != None:
            res = BST._path(root.left,data) 
            if res!=None:
                print(root.data)
            return res
        if root.data != None:
            if root.data == data:
                print(root.data)
                return root.data
        if root.right != None:
            res = BST._path(root.right,data) 
            if res!=None:
                print(root.data)
            return res

    def path(self,data):
        BST._path(self.root,data)



    def _realDeleteLeft(preRoot,rouge):
        root = preRoot.left
        if root.left == None and root.right == None:
            preRoot.left = None
        elif root.left == None or root.right == None:
            if root.left != None:
                preRoot.left = root.left
            else:
                preRoot.left = root.right
        else:
            left = root.left 
            right = root.right
            preRoot.left = None
            BST.insertNode(rouge,left)
            BST.insertNode(rouge,right)

    def _realDeleteRight(preRoot,rouge):
        root = preRoot.right
        if root.left == None and root.right == None:
            preRoot.right = None
        elif root.left == None or root.right == None:
            if root.left != None:
                preRoot.right = root.left
            else:
                preRoot.right = root.right
        else:
            left = root.left 
            right = root.right
            preRoot.right = None
            BST.insertNode(rouge,left)
            BST.insertNode(rouge,right)
            
            

    def _delete(root,data,rouge):
        if root.left != None:
            newroot = root.left
            if newroot.data == data:
                BST._realDeleteLeft(root,rouge)
            else:
                BST._delete(newroot,data,rouge)
        if root.right != None:
            newroot = root.right
            if newroot.data == data:
                BST._realDeleteRight(root,rouge)
            else:
                BST._delete(newroot,data,rouge)
  
        
    def dele(self,data):
        BST._delete(self.root,data,self.root)

    def _height(root,level):
        maxlevel = level
        if root.left != None:
            l = BST._height(root.left,level+1)
            if maxlevel < l:maxlevel=l
        elif root.right != None:
            l = BST._height(root.right,level+1)
            if maxlevel < l:maxlevel = l
        return maxlevel
            
        
    def height(self):
        return BST._height(self.root,0)

    def _depth(root,data):
        depth = None
        if root.left != None:
            d = BST._depth(root.left,data)
            if d != None:
                depth = d + 1
        if root.right != None:
            d = BST._depth(root.right,data)
            if d != None :
                depth = d + 1
        if root.data == data:
            depth = 0
        return depth

    def depth(self,data):
        return BST._depth(self.root,data)
    

    
        



# datainput = [int(e) for e in input('insert integers : ').split()]
# datainput = [random.randrange(30) for x in range(10)]
datainput = [9,15,2,4,18,8,1,3,10,20,0,-1]
print(datainput)
trees = BST()
for element in datainput:BST.insertR(trees.root,element)

# BST.inOrder(trees.root,lambda x:print(x,end=' '))
# for element in datainput[1:]:trees.dele(element)

trees.printSideway()
# print(trees.search())
# trees.inOrder()
print(trees.depth(15))