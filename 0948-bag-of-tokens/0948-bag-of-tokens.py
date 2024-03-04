class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        start = 0
        end = len(tokens) - 1
        score = 0 
        MaxScore = 0
        while start<=end:
            
            if power >= tokens[start]:
                score+=1
                power-=tokens[start]
                start+=1
                MaxScore = max(MaxScore, score)
            elif score>=1:
                score-=1
                power+=tokens[end]
                end-=1
            else:
                break
        return MaxScore