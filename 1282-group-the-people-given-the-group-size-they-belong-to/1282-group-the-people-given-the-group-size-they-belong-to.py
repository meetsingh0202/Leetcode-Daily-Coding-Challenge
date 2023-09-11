class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        groupSize = defaultdict(list)
        
        for index, val in enumerate(groupSizes):
            groupSize[val].append(index)
        
        res = []
        
        for key, val in groupSize.items():
            i = 0
            j = 0
            while i < len(val):
                temp = []
                j = i
                while j < i + key:
                    temp.append(val[j])
                    j += 1
                i = j
                res.append(temp)
        return res