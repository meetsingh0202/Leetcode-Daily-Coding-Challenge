class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        def traverse(index1, index2):
            if index1 == len(weights):
                return 0
            if index2 == len(weights):
                return 0
            
        if k == 1 or k == len(weights):
            return 0
        
        l = []
        for i in range(len(weights) - 1):
            a = weights[i]
            b = weights[i + 1]
            l.append(a + b)
        
        l.sort()
        x = sum(l[:k - 1])
        y = sum(l[-(k - 1):])
        # print(l[:k - 1])
        # print(l[-(k - 1):])
        return y -x