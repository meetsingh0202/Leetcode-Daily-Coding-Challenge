class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        # use binary search to find the first ice cream bar the boy can't afford
        left = 0
        right = len(costs) - 1
        while left <= right:
            mid = (left + right) // 2
            if costs[mid] > coins:
                right = mid - 1
            else:
                left = mid + 1

        # return the count of ice cream bars the boy can afford
        return len(costs) - left
