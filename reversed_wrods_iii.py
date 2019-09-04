class Solution:
    def reverseWords(self, s: str) -> str:
        sl=s.split(' ')
        
        r=[]
        for w in sl:
            r.append(w[::-1])
            
        return " ".join(r)
            

