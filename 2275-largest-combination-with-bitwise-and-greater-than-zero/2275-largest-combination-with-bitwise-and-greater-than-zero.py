class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        mapper = {i : 0 for i in range(24)}
        
        for num in candidates: 
            bit = str(bin(num))[2:][::-1]
            
            for i in range(len(bit)): 
                if bit[i] == "1":
                    mapper[i] += 1 

        return max(mapper.values())
