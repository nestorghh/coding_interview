class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        
        words = re.findall(r'\w+', paragraph.lower())
        
        dw = {}
        
        for w in words:
            if w not in banned :
                if w not in dw:
                    dw[w]=1
                else:
                    dw[w]+=1
         
        ans, best = ' ', 0
        for w in dw:
            if dw[w]>best:
                ans, best = w , dw[w] 
        return ans
    
        #return max(dw, key=lambda key: dw[key])



