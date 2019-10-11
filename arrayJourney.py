# Array journey @HackerRank

def solve(path,k):

	if len(path)==1:
		return path[0]

	opt={}
	for i in range(1,k+1):
		opt[-i] = 0

	opt[0] = path[0]

	for i in range(1, len(path)):
		opt[i] = max([path[i] + opt[i-x] for x in range(1,k+1)])

	return opt[len(path)-1]






