class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        HashMap = dict()
        for vote in votes:
            
            for i in range(len(vote)):
                currRank = i + 1
                currChar = vote[i]
                if currChar not in HashMap:
                    HashMap[currChar] = [0] * len(vote)
                    HashMap[currChar][i] += 1
                else:
                    HashMap[currChar][i] += 1
        
        voterNames = sorted(HashMap.keys())
        
        res = sorted(voterNames, key = lambda x : HashMap[x], reverse = True)
        
        return "".join(res)