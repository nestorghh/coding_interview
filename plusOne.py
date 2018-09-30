#plusOne problem @leetcode

def plusOne(digits):
	ni = int(''.join(map(str,digits)))+1
	return [int(d) for d in str(ni)]

a=plusOne([9])
b=plusOne([1,2,4,6])

print a, b

