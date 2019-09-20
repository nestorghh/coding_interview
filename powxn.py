class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #ans={}
        #if n<0:
        #    n=-n
        #    x=1/x
        
        #ans[0]=1
        
        #for i in range(1,n+1):
        #    ans[i]= ans[i-1]*x
        #return ans[n]
        
        if n<0:
            x=1/x
            n=-n
        
        if n==0:
            return 1
        
        h = self.myPow(x,n//2)
        if (n % 2 == 0):
            return h * h
        else:
            return x * h * h
