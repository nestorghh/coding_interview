def isIsomorphic(s: str, t: str) -> bool:
	seen = {}
	for i in range(len(s)):
		if s[i] in seen and seen[s[i]] != t[i]:
			return False

		if t[i] in seen.values() and s[i] != list(seen.keys())[list(seen.values()).index(t[i])]:
			return False
		seen[s[i]] = t[i]
	return True

s = 'ab'
t = 'aa'
print(isIsomorphic(s,t))

