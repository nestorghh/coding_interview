#Implement an algorithm to determine if a string has all unique 
#characters. What if you cannot use additional data structures?

def isunique(s):
	letters={}
	for c in s:
		if c in letters:
			return False
		letters[c]=True
	return True 

print(isunique('abcde'))
print(isunique('abacde'))
print(isunique('aabcde'))

# If not additional data structure can be used, we could solve 
#it by sorting the array first and then

def isunique2(s):
	s=sorted(s)
	for i in range(1,len(s)):
		if s[i]==s[i-1]:
			return False
	return True

print(isunique2('abcde'))
print(isunique2('abacde'))
print(isunique2('aabcde'))




