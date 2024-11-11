class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        
        currBoxes = 0
        currUnits = 0
        capacityToStore = truckSize
        
        for boxes, units in boxTypes:
            
            currLoad = min(boxes, capacityToStore)
            
            if currLoad > 0:
                currBoxes += currLoad
                currUnits += (currLoad * units)
                capacityToStore -= currLoad
                
        return currUnits