def isLongPressed(name,typed):
	import collections
	import itertools	

	# this doesn't work
	#a=collections.Counter(name)
	#b=collections.Counter(typed)
	
	a = [(k,len(list(grp))) for k, grp in itertools.groupby(name)] 
	b = [(k,len(list(grp))) for k, grp in itertools.groupby(typed)]

	if [x for (x,y) in a] == [x for (x,y) in b]:
	
		for i in range(len(a)):
			if a[i][1]>b[i][1]:
				return False		
		return True
				
	return False


print(isLongPressed('alex','aaleex'))
print(isLongPressed('saeed','ssaaedd'))
print(isLongPressed('laiden','laiden'))


#Runtime: 36 ms, faster than 70.03% of Python3 online submissions for Long Pressed Name.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Long Pressed Name.


