class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = collections.Counter(arr1)
        j = 0

        for i in arr2:
            for _ in range(count[i]):
                arr1[j] = i
                count[i] -=1
                j+=1 
            del count[i]       
        
        temp = []
        for i in count:
            for _ in range(count[i]):
                temp.append(i)
                count[i] -=1
        temp.sort()

        return arr1[:j] + temp[:] 
