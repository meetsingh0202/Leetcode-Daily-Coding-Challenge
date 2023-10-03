from sortedcontainers import *

class SummaryRanges:

    def __init__(self):
        self.treeMap = SortedDict()

    def addNum(self, value: int) -> None:
        self.treeMap[value] = True

    def getIntervals(self) -> List[List[int]]:
        res = []
        
        for i in self.treeMap:
            if res and res[-1][1] + 1 == i:
                res[-1][1] = i
            else:
                res.append([i, i])
        
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()