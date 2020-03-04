def findPivot(s,e,nums):
    m = (s+e)//2
    #print(s,e,m,nums[m],nums[m]>nums[m+1])
    if nums[m]>nums[m+1]:
        return m+1
    else:
        if nums[s] > nums[m]:
            return(findPivot(s,m-1,nums))
        else:
            return(findPivot(m+1,e,nums))

def binarySearch(nums,target):
    l, u = 0, len(nums)-1
    while l <= u:
        m = (l+u)//2
        if nums[m] < target:
            l = m + 1
        elif nums[m] == target:
            return m
        else:
            u = m - 1
    return -1


def search(nums, target):
    n = len(nums)-1
    pivot = findPivot(0,n,nums)

    if nums[pivot] == target:
        return pivot

    if nums[pivot]<=target<=nums[n]:
        return pivot + binarySearch(nums[pivot:n+1],target)
    else:
        return  binarySearch(nums[0:pivot],target)

