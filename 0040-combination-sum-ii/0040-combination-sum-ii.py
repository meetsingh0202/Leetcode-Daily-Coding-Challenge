class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def dfs(pos,temp,target):
            nonlocal prev
            if target==0:
                res.append(temp.copy())
            if target<=0:
                return
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                elif target - candidates[i] < 0:
                    break
                temp.append(candidates[i])
                dfs(i+1,temp,target-candidates[i])
                temp.pop()
                prev=candidates[i]
                
        prev=-1
        candidates.sort()
        dfs(0,[],target)
        return res