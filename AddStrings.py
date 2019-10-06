def addStrings(a,b):

	s=""
	i,j=len(a)-1,len(b)-1
	carry=0

	while i>=0 and j>=0:
		da=ord(a[i])-ord('0')
		db=ord(b[j])-ord('0')
		ds=da+db+carry

		if ds>=10:
			carry=1
		else:
			carry=0

		if i==0 and j==0:
			di=ds
		else:
			di=ds%10

		s=str(di)+s
		
		i-=1
		j-=1

	while i>=0:
		da=ord(a[i])-ord('0')
		ds=da+carry
		
		if ds>=10:
			carry=1
		else:
			carry=0

		if i==0:
			di=ds
		else:
			di=ds%10

		s=str(di)+s
		i-=1

	while j>=0:
		db=ord(b[j])-ord('0')
		ds=db+carry

		if ds>=10:
			carry=1
		else:
			carry=0
	
		if j==0:
			di=ds
		else:
			di=ds%10

		s=str(di)+s
		j-=1


	return s




