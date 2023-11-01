class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def traverse(row, col):
            HashSet.discard((row, col))
            
            for i in rows[row]:
                if (row, i) in HashSet:
                    traverse(row, i)
            
            for i in cols[col]:
                if (i, col) in HashSet:
                    traverse(i, col)
            
        if len(stones) == 1:
            return 0
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        HashSet = set()
        
        for i in stones:
            x, y = i
            
            rows[x].append(y)
            cols[y].append(x)
            HashSet.add((x, y))
            
        count = 0
        
        for i in range(len(stones)):
            x, y = stones[i]
            
            if (x, y) in HashSet:
                traverse(x, y)
                count += 1
        
        return len(stones) - count