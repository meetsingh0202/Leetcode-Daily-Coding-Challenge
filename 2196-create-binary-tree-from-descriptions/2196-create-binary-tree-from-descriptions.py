# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        adjacencyList = defaultdict(list)
        nodes, childNodes = set(), set()
        
        for i in descriptions:
            parent, child, isLeft = i
            adjacencyList[parent].append([child, isLeft])
            nodes.add(parent)
            nodes.add(child)
            childNodes.add(child)
            
        root = None
        for node in nodes:
            if node not in childNodes:
                root = TreeNode(node)
        
        # print(adjacencyList)
        
        def traverse(currNode):
            for childNode, isLeft in adjacencyList.get(currNode.val, []):
                child = TreeNode(childNode)
                if isLeft:
                    currNode.left = child
                else:
                    currNode.right = child
                traverse(child)
            
        traverse(root)
        return root
