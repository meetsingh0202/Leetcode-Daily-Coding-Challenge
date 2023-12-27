class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last = colors[0]
        lastCost = neededTime[0]
        lastIndex = 0
        i = 1
        totalCost = 0

        while i < len(colors):
            currColor = colors[i]
            currCost = neededTime[i]
            if currColor == last:
                if currCost < lastCost:
                    totalCost += currCost
                    i += 1
                    continue
                else:
                    totalCost += lastCost
                    lastIndex = i
                    lastCost = currCost
                    last = currColor
                    i += 1
            else:
                last = currColor
                lastCost = currCost
                lastIndex = i
                i += 1

        return totalCost
            
