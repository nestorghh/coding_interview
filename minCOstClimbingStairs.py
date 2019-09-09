def minCostClimbing(cost):

	dp={}
	dp[0]=cost[0]
	dp[1]=cost[1]
	n=len(cost)

	for i in range(2,n):
		dp[i] = cost[i] + min(dp[i-1], dp[i-2])

	return min(dp[n-1], dp[n-2])

