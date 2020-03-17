def reverseArray(nums):
    s, e = 0, len(nums)-1

    while s < e:
        nums[s], nums[e] = nums[e], nums[s]
        s+=1
        e-=1

    return nums

