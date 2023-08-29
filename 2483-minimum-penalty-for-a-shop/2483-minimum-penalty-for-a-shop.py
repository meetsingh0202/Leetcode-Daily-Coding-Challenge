class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = cur_penalty = sum([1 for c in customers if c == 'Y'])
        ans = 0
        for i, c in enumerate(customers):
            if c == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                ans = i + 1
        
        return ans