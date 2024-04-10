class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        indices = deque(range(len(deck)))
        
        result = [0] * len(deck)
        
        for card in deck:
            idx = indices.popleft()
            result[idx] = card
            
            if indices:
                indices.append(indices.popleft())
        
        return result
