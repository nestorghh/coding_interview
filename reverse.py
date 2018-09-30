#leetcode problem reverse integer
def reverse(inte):
	ints=str(inte)
	if ints[0]=='-':
		suma=0
		ints=ints[1:len(ints)]
		coef=[int(d) for d in ints]
		for i in range(len(coef)):
			suma=suma+(coef[i]*(10**i))
		suma=-1*suma
	else:
		suma=0
		coef=[int(d) for d in ints]
		for i in range(len(coef)):
			suma=suma+(coef[i]*(10**i))
	if(abs(suma) > (2 ** 31 - 1)):
		return 0
	else:
		return suma
	
a=reverse(433)
b=reverse(123)
c=reverse(-123)
d=reverse(120)
e=reverse(1534236469)

print a,b,c,d,e



