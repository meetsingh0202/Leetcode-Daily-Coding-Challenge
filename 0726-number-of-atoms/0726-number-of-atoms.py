class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0

        while i<len(formula):
            if formula[i]=='(':
                stack.append(defaultdict(int))
            elif formula[i]==')':
                cur_map = stack.pop()
                count = ""
                while i+1<len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i+=1
                prev_map = stack[-1]
                count = 1 if not count else int(count)
                for ele in cur_map:
                    prev_map[ele] += cur_map[ele]*count
            else:
                element = formula[i]
                count = ""
                if i+1<len(formula) and formula[i+1].islower():
                    element  = formula[i:i+2]
                    i+=1
                while i+1<len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i+=1
                count = 1 if not count else int(count)
                cur_map = stack[-1]
                cur_map[element]+=count
            i+=1
        
        res_map = stack[-1]
        ans = ""
        for h in sorted(res_map.keys()):
            cnt = "" if res_map[h]==1 else res_map[h]
            ans += h+str(cnt)
        return ans
