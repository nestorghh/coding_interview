class Solution():
    def searchRange(self,nums,target):
        l, u = 0, len(nums)-1

        while l<=u:
            m=(l+u)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                u=m-1
        return -1

