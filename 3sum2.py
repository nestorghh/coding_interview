def threesum(nums):
	
	table=[]
	for i, v in enumerate(nums):
		table.append((i,v))

	count=0
	ele=[i[1] for i in table]
	print(ele)
	t=[]
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			val = -nums[i]-nums[j]
			if val in ele and val!=nums[i] and val!=nums[j]:
				count+=1
				t.append([nums[i],nums[j],val])
				print(t)
				ele=list(filter(lambda a: a != nums[i], ele))
				ele=list(filter(lambda a: a != nums[j], ele))
				ele=list(filter(lambda a: a != val, ele))
				#pop elements i,j,val from ele 		
	return count

