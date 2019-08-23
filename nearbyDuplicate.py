#Given an array of integers and an integer k, find out whether there are two distinct 
#indices i and j in the array such that nums[i] = nums[j] and the absolute 
#difference between i and j is at most k.
class Solution:
    #def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #    n=len(nums)
    #    count=0
    #    for i in range(n-1):
    #        for j in range(i+1,n):
    #            if nums[i]==nums[j] and abs(i-j)<=k:
    #                count+=1
    #    return count>0
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        
        for i, v in enumerate(nums):
            if d.get(v,-1)>=0:
                diff = abs(d[v]-i)
                if diff<=k:
                    return True
            d[v]=i
        return False
