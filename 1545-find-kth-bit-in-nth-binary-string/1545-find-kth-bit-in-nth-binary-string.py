class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(bits: str) -> str:
            return ''.join('1' if bit == '0' else '0' for bit in bits)
        def reverse(s: str) -> str:
            return s[::-1]
        
        s = "0"
        for i in range(2, n+1):
            s = s + '1' + reverse(invert(s))
        return s[k - 1]
