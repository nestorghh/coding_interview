def mergeKLists(lists):
	x=[]

	while lists:
		minVal = min([lists[i].data for i in range(len(lists))])
		index = 0
		for l in lists:
			if l.data == minVal:
				x.append(l)
				if l.next is None:
					lists.remove(l)
				else:
					lists[index].next = l.next
				break
			index+=1






