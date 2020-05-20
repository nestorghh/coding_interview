class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        minA = min(self.numSwap(A,B,A[0]),self.numSwap(A,B,B[0]))
        minB = min(self.numSwap(B,A,A[0]),self.numSwap(B,A,B[0]))
        minRes = min(minA,minB) 
        
        return -1 if minRes==float('Inf') else minRes
    
    def numSwap(self, A,B,target):
        numSwap=0
        for i in range(len(A)):
            if (A[i]!=target) and (B[i]!=target):
                return float('Inf')
            elif A[i]!=target:
                numSwap+=1
        return numSwap
