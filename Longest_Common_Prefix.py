class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort() #Ascending order
        print("sorted_strs", strs)
        prefix1 = ""
        prefix2 = ""
        
        i = 2
        print("strs[-1]:", strs[-1])
        for x, y in zip(strs[0], strs[-1]):
            print('x: ', x)
            print("y: ", y)
            if x == y:
                prefix1 += x
            else:
                break
        
        if len(strs) > 2:
            for p, y in zip(prefix1, strs[-i]):
                if p == y:
                    prefix2 += p
                
                if i < -len(strs)+1:
                    break
                    
            return "".join(prefix2)
        else:
            return "".join(prefix1)
        
        