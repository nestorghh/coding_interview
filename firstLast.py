class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return [self.findFirst(nums,target),self.findLast(nums,target)]
        
    def findFirst(self,nums,target):    
        l, u = 0, len(nums)-1
        index = -1
        
        while l<=u:
            m=(l+u)//2
            if nums[m]>=target:
                u = m-1
            else:
                l = m+1
        
            if nums[m]==target:
                index = m
        return index
                
    def findLast(self,nums,target):    
        l, u = 0, len(nums)-1
        index = -1
        
        while l<=u:
            m=(l+u)//2
            if nums[m]<=target:
                u = m +1
            else:
                l=m-1
        
            if nums[m]==target:
                index = m
        return index
        
