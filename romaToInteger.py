class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        i=n-1
        res=d[s[n-1]]
        while i>0:
            if d[s[i-1]]<d[s[i]]:
                res += -d[s[i-1]]
                #print(s[i-1],s[i])
                #print(d[s[i-1]], d[s[i]])
                #res += (d[s[i]] - d[s[i-1]])
                #print(d[s[i]] - d[s[i-1]])
            else:
                #print(s[i-1],s[i])
                #print(d[s[i-1]], d[s[i]])
                #res += (d[s[i]] + d[s[i-1]])
                #print(d[s[i]] + d[s[i-1]])
                res += d[s[i-1]]
            i-=1
            #if i==0:
            #    res += d[s[i]]
            
        return res
            
