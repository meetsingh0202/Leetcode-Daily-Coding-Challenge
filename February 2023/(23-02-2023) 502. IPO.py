class MyNode(object):
    def __init__(self, priority, profit, capital):
        self.priority = priority
        self.profit = profit
        self.capital = capital

    def __repr__(self):
        return f'Node value: {self.priority, self.profit, self.capital}'

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.profit == other.profit:
            return self.capital >= other.capital
        else:
            return self.profit > other.profit
            
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        heap = []
        
        for i in range(len(profits)):
            tempNode = MyNode(0, profits[i], capital[i])
            heappush(heap, tempNode)
                    
        currCapital = w
        count = 0
        newPriorityVal = float('inf')
        lastPriority = -1
        
        while heap:
            tempNode = heappop(heap)
            currPriority, currProfit, currCapitalRequired = tempNode.priority, tempNode.profit, tempNode.capital

            if currCapital >= newPriorityVal and currPriority == lastPriority:
                heappush(heap,  MyNode(currPriority + 1, currProfit, currCapitalRequired))
                continue
            
            if currCapitalRequired <= currCapital:
                currCapital += currProfit
                k -= 1
                if k == 0:
                    return currCapital
                count = 0
            else:
                newPriorityVal = currCapitalRequired
                lastPriority = currPriority
                heappush(heap,  MyNode(currPriority + 1, currProfit, currCapitalRequired))
                count += 1
                if count == len(heap):
                    return currCapital
        return currCapital
