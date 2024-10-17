class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = [x for x in str(num)]
        target = sorted(num, reverse=True)
        for i in range(len(num)):
            if int(num[i])!=int(target[i]):
                for j in range(len(num)-1, i,-1):
                    if int(num[j])==int(target[i]):
                        num[i], num[j] = num[j], num[i]
                        return int(''.join(num))
        return int(''.join(num))
