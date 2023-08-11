class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def traverse(currIndex, currAmount):
            if currAmount == amount:
                return 1
            
            if currIndex == len(coins) or currAmount > amount:
                return 0
            
            currCoin = coins[currIndex]
            take, notTake = 0, 0
            
            if currCoin + currAmount <= amount:
                take = traverse(currIndex, currAmount + currCoin)
            
            notTake = traverse(currIndex + 1, currAmount)
            
            return take + notTake
        
        return traverse(0, 0)
            