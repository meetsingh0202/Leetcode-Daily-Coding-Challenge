class Solution:
    def minSwaps(self, s: str) -> int:
        
        one = s.count("1")
        zero = s.count("0")
        
        if (abs(one - zero) > 1):
            return -1
        
        def solve(s, ch):
            res = 0
            for i in range(len(s)):
                if (ch != s[i]):
                    res += 1
                    
                if ch == "1":
                    ch = "0"
                else:
                    ch = "1"
                    
            return res // 2
        
        if zero > one:
            return solve(s, "0")
        elif (one > zero):
            return solve(s, "1")
        else:
             return min(solve(s, "0"), solve(s, "1"))
