# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.l = self._flatten(nestedList)
        self.i = -1
        
    def _flatten(self, list1):
        l2 = []
        for element in list1:
            if element.isInteger():
                l2.append(element.getInteger())
            else:
                l2.extend(self._flatten(element.getList()))
        return l2

    def next(self):
        self.i += 1
        return self.l[self.i]

    def hasNext(self):
        return self.i < len(self.l) - 1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())