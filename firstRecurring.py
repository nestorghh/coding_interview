def firstRecurring(s):
	d={}
	for i in s:
		if i in d:
			return i
		else:
			d[i]=1
		
	return None

print(firstRecurring('DBCABA'))
print(firstRecurring('ABC'))
print(firstRecurring('ABCA'))


