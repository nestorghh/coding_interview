class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        i,j = 0, 0
        n,m = len(pushed), len(popped)
        stack = []
        
        while i<n and j<m:
            stack.append(pushed[i])
            
            while stack and j<m and stack[-1]==popped[j]:
                stack.pop()
                j+=1
            i+=1
            
        return j==m
