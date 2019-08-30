def int_to_str(n):

	l=[]	

	is_negative=False

	if n<0:
		n, is_negative= -n, True

	while True:
		l.append(chr(ord('0')+n%10))
		n=n//10
		if n==0:
			break
	
	return  ('-' if is_negative else '') + ''.join(reversed(l))

def str_to_int(s):
	import string

	is_negative=False
	n = len(s)

	if s[0]=="-":
		is_negative=True

	
	if is_negative:
		s=s[1:]
		n=len(s)

	inte=0
	for i in range(len(s)):
		inte+=string.digits.index(s[i])*10**(n-1-i)
		
	return inte * (-1 if is_negative else 1)



