class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        nums = []
        i, j = 0 , 0
        
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        
        while i<n:
            nums.append(nums1[i])
            i+=1
        
        while j<m:
            nums.append(nums2[j])
            j+=1
        
        pivot = len(nums)//2
        
        if len(nums)%2!=0:
            return nums[pivot]
        else:
            return (nums[pivot] + nums[pivot-1])/2

