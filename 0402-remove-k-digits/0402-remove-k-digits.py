class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        if not k:
            return num
        arr = []
        for n in num:
            while arr and arr[-1] > n and k:
                arr.pop()
                k -= 1
            arr.append(n)
            if len(arr) == 1 and arr[-1] == '0':
                arr.pop()
        while k and arr:
            arr.pop()
            k -= 1
        return "".join(arr) if arr else "0"
