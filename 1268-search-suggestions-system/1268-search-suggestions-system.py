class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    
        left = 0
        right = len(products) - 1
        
        res = []
        
        products.sort()
        
        for i in range(len(searchWord)):
            currChar = searchWord[i]
            
            while left <= right and (len(products[left]) <= i or products[left][i] != currChar):
                left += 1
                
            while left <= right and (products[right][i] != currChar):
                right -= 1
            
            windowLength = right - left + 1
            
            temp = []
            
            for j in range(min(3, windowLength)):
                temp.append(products[left + j])
                
            res.append(temp)
    
        return res