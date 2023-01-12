class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()

        # keep track of the number of ice cream bars bought
        count = 0

        # iterate through the costs and add up the number of ice cream bars the boy can buy
        for cost in costs:
            if cost <= coins:
                count += 1
                coins -= cost
            else:
                return count

        # return the final count
        return count
