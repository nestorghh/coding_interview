def employeeFreeTime(schedule):

	# we sort schedule by starting time
	sortedSchedule=[]
	for i in range(len(schedule)):
		for j in range(len(schedule[i])):
			sortedSchedule.append(schedule[i][j])

	sortedSchedule.sort(key= lambda x: x[0])

	result=[sortedSchedule[0]]

	for i in range(1,len(sortedSchedule)):
		print(i)
		if result[-1][1] >= sortedSchedule[i][0]:
			print('greater')
			result[-1]=[result[-1][0], max(result[-1][1],sortedSchedule[i][1])]
			print(result)
		else:
			print('disjoint')
			result.append(sortedSchedule[i])
			print(result)

	ans=[]
	for i in range(len(result)-1):
		ans.append([result[i][1],result[i+1][0]])
	
	return ans

