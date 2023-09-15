from queue import Queue

class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()


    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def minBST(self):
      current = self
      while current.left:
        current = current.left
      print("Minimum Value: ", current.value)
      
    def maxBST(self):
      current = self
      while current.right:
        current = current.right
      print("Maximum Value: ", current.value)
    
    def sumBST(self): #Couldn't figure out the sum of lower values so this will have to do :(
      if self is None:
          return 0
      Q = Queue()
      Q.put(self)
      currentSum = 0
      while not Q.empty():
          node = Q.get()
          if node is None:
              continue
          currentSum = currentSum + node.value
          Q.put(node.left)
          Q.put(node.right)
      print("Sum of nodes: ", currentSum)
    
    """
    def findSubTree(self, value):
      value = input("hi")
      if value == self.value: 
           pass
      if value > self.value: 
           pass
      if value < self.value: 
           pass
      else:
        return "value not found"
        
    def sumBeneath(t, value):
      tree = findSubtree(t, value)
      s = 0
      if tree.left is not None:
           s += tree.left.sum_tree()
      if tree.right is not None:
           s += tree.right.sum_tree()
      return s
    """
    
    def count(self):
        if self is None:
            return 0

        stack = Stack()
        stack.push(self)
        count = 1
        while stack:
            node = stack.pop()
            if node.left:
                count += 1
                stack.push(node.left)
            if node.right:
                count += 1
                stack.push(node.right)
        print("Amount of Nodes: ", count)

def printTree(n, indent = 0):
    if n.right is not None:
        printTree( n.right, indent + 4)
    print( " " * indent, end = "")
    print(n.value)
    if n.left is not None:
        printTree( n.left, indent + 4)
        
class example_BST:
  #inefficent way, but it helped me visualize what I was creating better
  root = BST(25)
  
  root.left = BST(20)
  root.right = BST(36)
  
  root.left.left = BST(10)
  root.left.right = BST(22)
  
  root.right.left = BST(30)
  root.right.right = BST(40)

  root.left.left.left = BST(5)
  root.left.left.right = BST(12)
  
  root.left.left.left.left = BST(1)
  root.left.left.left.right = BST(8)
  
  root.left.left.left.right.right = BST(9)
  
  root.left.left.left.left.left = BST(-10)
  root.left.left.left.left.right = BST(4)
  
  root.right.left.left = BST(28)
  
  root.right.right.left = BST(38)
  root.right.right.right = BST(48)
  
  root.right.right.right.left = BST(45)
  root.right.right.right.right = BST(50)
  
  root.right.right.right.right.right = BST(100)

  print("Printng Tree: ")
  printTree(root)
  print("\n")
  root.minBST()
  print("\n")
  root.maxBST()
  print("\n")
  root.count()
  print("\n")
  root.sumBST()