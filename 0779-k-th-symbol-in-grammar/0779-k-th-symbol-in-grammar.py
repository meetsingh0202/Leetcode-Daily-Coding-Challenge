class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def traverse(currN, currK):
            if currN == 1 or currK == 1:
                return 0
            
            lastColoumnElements = (2 ** (currN - 1)) // 2 
            
            if currK <= lastColoumnElements:
                return traverse(currN - 1, currK)
            else:
                return 1 - traverse(currN - 1, currK - lastColoumnElements)
        
        return traverse(n, k)