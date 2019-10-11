class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import Counter
    
        csplit = [l.split() for l in cpdomains]
    
        result=collections.Counter()
        
        r=[]
        
        for c in csplit:
            
            count, domain = int(c[0]), c[1]
            
            current = domain.split(".")
            
            for i in range(len(current)):
                result[".".join(current[i:])] += count
                
        
        for d, c in result.items():
            r.append(str(c)+" "+d)
        
        return r


