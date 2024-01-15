class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        Winner = dict()
        Looser = dict()
        res = [[], []]
        
        for i in matches:
            winner, looser = i
            
            if looser in Winner:
                del Winner[looser]
                
            Looser[looser] = 1 + Looser.get(looser, 0)
            
            if winner not in Looser and winner not in Winner:
                Winner[winner] = 1
        
        for winner in Winner:
            res[0].append(winner)
        
        for looser, losses in Looser.items():
            if losses == 1:
                res[1].append(looser)
        
        res[0].sort()
        res[1].sort()
        
        return res
        