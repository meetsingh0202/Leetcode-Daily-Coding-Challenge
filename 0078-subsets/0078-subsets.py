class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        def traverse(currIndex, currSubarray):
            total.append(currSubarray)
            for i in range(currIndex, len(A)):
                traverse(i + 1, currSubarray + [A[i]])
        
        total = []
        A.sort()
        traverse(0, [])
        return total