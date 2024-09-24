class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        s1 = set()
        arr1, arr2 = [str(n1) for n1 in arr1], [str(n2) for n2 in arr2]
        res = 0
        
        for num1 in arr1:
            prefix = ""
            for d in num1:
                prefix += d
                s1.add(prefix)

        for num2 in arr2:
            prefix = ""
            temp = 0
            for d in num2:
                prefix += d
                if prefix in s1:
                    temp += 1
            res = max(res, temp)

        return res
