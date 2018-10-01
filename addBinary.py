# 67. Add Binary

#Given two binary strings, return their sum (also a binary string).
#The input strings are both non-empty and contains only characters 1 or 0.

def addBinary(a,b):
	mlen = max(len(a),len(b))

	if len(a) < mlen:
		a = '0'*(mlen -len(a)) + a
		print(a)
	
	if len(b) < mlen:
		b = '0'* (mlen - len(b)) + b 
		print(b)
	
	result = ''
	carry = 0

	for i in range(mlen-1,-1,-1):
		r = carry
		r = r +1 if a[i] == '1' else r
		r = r +1 if b[i] == '1' else r

		result = ('1' if r%2 ==1 else '0') + result
		carry = 0 if r<2 else 1 
		print('result',result)
		print('carry',carry)
	if carry!=0:
		result = '1' + result

	return result
		
# the pythonic solution 

def addBinary_python(a,b):
	return bin(int(a,2) + int(b,2))	






