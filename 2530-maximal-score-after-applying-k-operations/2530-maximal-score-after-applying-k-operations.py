class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heappush(heap, -i)
            
        score = 0
        while heap:
            curr = - heappop(heap)
            if k:
                score += curr
                temp = ceil(curr / 3)
                heappush(heap, - temp)
                k -= 1
            else:
                break
            # print(k, score, heap)
        return score