class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        HashMap = dict()
        for i in arr:
            HashMap[i] = 1 + HashMap.get(i, 0)
        
        val = list(HashMap.values())
        valSet = set(val)
        if len(val) == len(valSet):
            return True
        return False