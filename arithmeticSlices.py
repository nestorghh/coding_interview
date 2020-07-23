def numberOfArithmeticSlices(nums):

    B, n = [0]*len(nums), len(nums)

    for i in range(2,n):

        if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
            B[i] = 1 + B[i-1] 
            
    return sum(B)



