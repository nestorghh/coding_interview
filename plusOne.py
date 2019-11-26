#plusOne problem @leetcode

# the not-so-good way
def plusOne(digits):
	ni = int(''.join(map(str,digits)))+1
	return [int(d) for d in str(ni)]

a=plusOne([9])
b=plusOne([1,2,4,6])

print(a,b)

# the way to go

def plusOne2(digits):
	digits[-1]+=1
	
	for i in reversed(range(1,len(digits))):
		if digits[i]!=10:
			break
		digits[i]=0
		digits[i-1]+=1

	if digits[0]==10:
		digits[0]=1
		digits.append(0)

	return digits
	
		
a=plusOne2([9,9])
b=plusOne2([1,2,4,6])
c=plusOne2([1,5,9])

print(a,b,c)





