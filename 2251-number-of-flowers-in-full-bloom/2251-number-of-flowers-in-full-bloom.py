class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        
        for i in range(len(people)):
            index, val = i, people[i]
            people[i] = [val, index]
            
        people.sort()
        
        # print(flowers)
        # print(people)
        
        heap = []
        
        startTime = people[0][0]
        flowerIndex = 0
        
        while flowerIndex < len(flowers):
            if startTime >= flowers[flowerIndex][0] and flowers[flowerIndex][1] >= startTime:
                heappush(heap, flowers[flowerIndex][1])
                flowerIndex += 1
            elif startTime >= flowers[flowerIndex][0] and startTime >= flowers[flowerIndex][1]:
                flowerIndex += 1
            else:
                break

        res = [0] * len(people)
        
        res[people[0][1]] = len(heap)
        
        # print(heap)
        
        for val, index in people[1:]:
            # print("START : ", val, heap)
            
            while heap and heap[0] < val:
                heappop(heap)
                
            currTime = val
            # print(val, flowers[flowerIndex:])
            
            while flowerIndex < len(flowers):
                if currTime >= flowers[flowerIndex][0] and flowers[flowerIndex][1] >= currTime:
                    heappush(heap, flowers[flowerIndex][1])
                    flowerIndex += 1
                elif currTime >= flowers[flowerIndex][0] and currTime >= flowers[flowerIndex][1]:
                    flowerIndex += 1
                else:
                    break
            
            res[index] = len(heap)
        
            # print("END : ", val, heap)
            
        return res
            
        
        