def findMinAmplitude(nums):
    
    n=len(nums)
    nums=sorted(nums)

    if n<=4:
        return 0
    else:
        minAmp = float('Inf')

        for i in range(0,4):
            minAmp = min(minAmp,nums[n-1-i]-nums[3-i])

    return minAmp




