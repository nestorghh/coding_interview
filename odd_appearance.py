def oddNumber(nums):
    n = len(nums)-1
    res=0
    for i in range(0,n):
        res ^= nums[i]

    return res

