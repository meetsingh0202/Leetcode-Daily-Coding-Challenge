class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        HashMap = defaultdict(set)
        count = 0
        
        for i in ideas:
            HashMap[i[0]].add(i[1:])
        
        for key1, val1 in HashMap.items():
            for key2, val2 in HashMap.items():
                if key1 == key2:
                    continue
                    
                currLen = len(val1 & val2)
                firstPairs = len(val1) - currLen
                secondPairs = len(val2) - currLen
                count += (firstPairs * secondPairs)
        
        return count
