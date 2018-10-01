#151. Reverse words in a string

#Given an input string, reverse the string word by word.

def reverseWords(s):

	s = s.strip()

	if len(s)<=1:
		return s

	s = s.split()

	rs=''

	for w in s[(len(s)-1):0:-1]:
		rs+= w + ' '
	rs += s[0]
	
	return rs


