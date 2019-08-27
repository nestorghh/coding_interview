def relativeSortArray(array1,array2):

	d={}
	for e in array1:
		if e not in d:
			d[e]=1
		else:
			d[e]+=1
	narray1=[]
	
	for e in array2:
		if e in d:
			narray1=narray1+[e]*d[e]
	non=[]	
	for e in array1:
		if e not in array2 and e not in non:
			non=non+[e]*d[e]
	
	non=sorted(non)

	return narray1+non
			
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]	

