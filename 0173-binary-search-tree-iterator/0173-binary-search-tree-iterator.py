# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            self.arr.append(root.val),
            self.printInorder(root.right)
            
    def __init__(self, root):
        self.arr = [0]
        self.root = root
        self.printInorder(self.root)
        self.index = 0
        
    def next(self):
        self.index += 1
        currVal = self.arr[self.index]
        return currVal
    
    def hasNext(self):
        if self.index >= len(self.arr) - 1:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()