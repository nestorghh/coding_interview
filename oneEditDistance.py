def isOneEditDistance(s,t):

	m, n = len(s), len(t)


	if abs(m-n)>1:
		return False

	if n<m:
		s, t = t, s

	# Let's assume that s is always shorter or the same length as t.

	for i in range(len(s)):
		
		if s[i]!=t[i]:
			
			if m==n:
				return s[i+1:]==t[i+1:]

			else:
				return s[i:]==t[i+1:]

	return abs(m-n)==1	

