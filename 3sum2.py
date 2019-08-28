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
				#pop elements i,j,val 		
	return count

