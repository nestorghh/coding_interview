# Leetcode #14: Longest common prefix


def lcp(words):
	p=''
	if len(words)==0:
		return p
	w0=words[0]
	m=min([len(w) for w in words])
	i=1
	for l in range(m):
		c=0
		while ( (i<len(words)) and (w0[l]==words[i][l])):
			c+=1
			i+=1
		if c==len(words)-1:
			p+=w0[l]
		else:
			return p 
		i=1
	return p
	


print(lcp(['flower','flow','flight']))
print(lcp(['carla','caren','carro','cartera']))
print(lcp(['carla','caren','carro','cartera','na']))
print(lcp(['dog','racecar','car']))

#Runtime: 40 ms, faster than 63.76% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 13.1 MB, less than 91.92% of Python3 online submissions for Longest Common Prefix.



