#1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        from collections import deque
        
        minQueue = deque([])
        maxQueue = deque([])
        s, e = 0, 0
        ans = 0
        
        while e<len(nums):
            
            x = nums[e]
            
            while minQueue and nums[minQueue[-1]]>=x:
                minQueue.pop()
                
            minQueue.append(e)
            
            while maxQueue and nums[maxQueue[-1]]<=x:
                maxQueue.pop()
                
            maxQueue.append(e)
            
            mini = nums[minQueue[0]]
            maxi = nums[maxQueue[0]]
            
            if maxi - mini>limit:
                s+=1
                if s>minQueue[0]:
                    minQueue.popleft()
                if s>maxQueue[0]:
                    maxQueue.popleft()
            else:
                ans = max(ans,e-s+1)
                e+=1
                
        return ans
