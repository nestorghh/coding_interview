def findContentChildren(g,s):
	s.sort()
	g.sort()
	child,i,j=0,0,0
	while ((i<=len(g)-1) and (j<=len(s)-1)):
		if g[i]<=s[j]:
			child+=1
			i+=1
			j+=1
		else:
			j+=1
	return child

print(findContentChildren([1,2,3],[1,1]))
print(findContentChildren([1,2],[1,2,3]))
print(findContentChildren([5,4,3,2],[1,6,1,6]))
print(findContentChildren([10,9,8,7],[5,6,7,8])) 

#Runtime: 68 ms, faster than 92.21% of Python3 online submissions for Assign Cookies.
#Memory Usage: 14.6 MB, less than 34.06% of Python3 online submissions for Assign Cookies.


