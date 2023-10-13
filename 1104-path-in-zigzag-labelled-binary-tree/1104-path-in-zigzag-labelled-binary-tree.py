class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        def findLevel(x):
            n = 0

            while 2 ** n <= x:
                n += 1

            return n - 1
        
        def findStartEnd(level):
            startPos = 2 ** level
            endPos = (2 ** (level + 1)) - 1
            
            return [startPos, endPos]
        
        
        level = findLevel(label)
        startPos, endPos = findStartEnd(level)
        res = [label]
        
        currNode = label
        
        while currNode > 1:
            currLevel = findLevel(currNode)
            startPos, endPos = findStartEnd(currLevel)
            # print("START : ", startPos, " END : ", endPos, "CURRNODE : ", currNode, "CURRLEVEL : ", currLevel)
            
            if currLevel % 2:
                correspondingNode = startPos + (endPos - currNode)
                # print(currNode, correspondingNode)               
                currNode = correspondingNode // 2
            else:
                correspondingNode = endPos - (currNode - startPos)
                # print(currNode, correspondingNode)
                currNode = correspondingNode // 2
                
            res.append(currNode)
        
        return res[::-1]
            
            
        