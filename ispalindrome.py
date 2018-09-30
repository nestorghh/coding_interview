#isPalindrome problem leetcode
#recursive solution 
def isPalindrome(x):
	x=str(x)
	if len(x)<2:
		return True
	elif x[0]!=x[-1]:
		return False
	return isPalindrome(x[1:-1])

a=isPalindrome('madam')
b=isPalindrome('nursesrun')
c=isPalindrome('vee')
d=isPalindrome(1221)

print a,b,c,d

#nonrecursive solution. Just check that the word is equal to itself reversed.
def isPalindrome2(x):
	x=str(x)
	if x==x[::-1]: 
		return True
	else:
		return False

a=isPalindrome2('madam')
b=isPalindrome2('nursesrun')
c=isPalindrome2('vee')
d=isPalindrome2(1221)

print a,b,c,d



