def zigZag(nums):
    n = len(nums)-2
    flag = True

    for i in range(0,n+1):

        if flag==True:
        
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            if nums[i]<nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        flag = not flag

    return nums

