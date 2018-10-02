#Suppose you are at a party with $n$ people (labeled from $0$ to $n - 1$) and among them, 
#there may exist one celebrity. The definition of a celebrity is that all the 
#other $n - 1$ people know him/her but he/she does not know any of them. 
#Your task is to find the stranger (celebrity) in party.

def findCelebrity(G):

	i = 0
	j = len(G[0])-1

	while i < j:
		if G[i][j]==1:
			i+=1
		#	print('i is ',i)
		else:
			j-=1
		#	print('j is ',j)

	
	for i in range(len(G)):
		if i!=j and (G[i][j] == 0 or G[j][i]==1):
			return -1
	return 1 
	



G1=[[0,1,1],[1,0,1],[0,0,0]]

G2=[[0,1,1],[0,0,0],[1,1,0]]

print(findCelebrity(G1))
print(findCelebrity(G2))


