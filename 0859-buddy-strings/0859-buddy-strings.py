class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False

        diff = [(a, b) for a, b in zip(s, goal) if a != b]

        if len(diff) == 0 and len(s) > len(set(s)):
            return True

        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]
