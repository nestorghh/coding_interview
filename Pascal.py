#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle

def getPascal(n):

	if n==0:
		return []	

	L=[]
	ini = [0,1,0]
	
	for i in range(n-1):
		l=[ini[k]+ini[k+1] for k in range(len(ini)-1)]
		L.append(l)
		ini=[0]+l+[0]	
	return [[1]]+L





