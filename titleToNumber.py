def titleToNumber(s):
	
	suma = 0

	for c in s:
		suma = 26*suma + ord(c) - ord('A') +1

	return suma




