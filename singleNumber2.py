#137. Single Number II

def singleNumber(nums):
        missing = (3*sum(set(nums))-sum(nums))//2
        return missing

print(singleNumber([2,2,3,2]))
print(singleNumber([0,1,0,1,0,1,99]))


#Runtime: 32 ms, faster than 98.02% of Python3 online submissions for Single Number II.
#Memory Usage: 14.6 MB, less than 37.70% of Python3 online submissions for Single Number II.
