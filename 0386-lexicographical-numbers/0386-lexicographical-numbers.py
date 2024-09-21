class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        temp = []
        for i in range(1, n + 1):
            temp.append(str(i))
        
        temp.sort()
        
        return [int(i) for i in temp]