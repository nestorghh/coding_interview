def majority(numbers):
	d={}
	for i in range(len(numbers)):
		if numbers[i] in d:
			d[numbers[i]]+=1
		else:
			d[numbers[i]]=1

	return max(d,key=d.get)

print(majority([3,2,3]))
print(majority([2,2,1,1,1,2,2]))

#Runtime: 52 ms, faster than 64.65% of Python3 online submissions for Majority Element.
#Memory Usage: 14.4 MB, less than 51.79% of Python3 online submissions for Majority Element.


