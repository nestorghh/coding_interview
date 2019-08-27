mem = []
def isHappy(n):
	ns=str(n)
	suma=0
	for d in ns:
		suma+=int(d)**2

	if suma==1:
		return True

	if suma in mem:
		return False

	mem.append(suma)
	
	return isHappy(suma)


