def checkPangram(s):
	List = []
	for i in range(26):
		List.append(False)

	for c in s.lower():
		if not c== ' ':
			List[ord(c)-ord('a')]=True # Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object

	for ch in List:
		if ch ==False:
			return False
	return True

print (checkPangram('The quick brown fox jumps over the little lazy dog'))

