def max_profit(prices):
	maxi=0
	for i in range(1,len(prices)):
		if prices[i]-prices[i-1]>0:
			maxi+=prices[i] - prices[i-1]
	return maxi

print(max_profit([7,1,5,3,6,4]))
print(max_profit([1,2,3,4,5]))
print(max_profit([7,6,4,3,1]))

#Runtime: 36 ms, faster than 94.15% of Python3 online submissions for Best Time to Buy and Sell Stock II.

#Memory Usage: 13.7 MB, less than 96.71% of Python3 online submissions for Best Time to Buy and Sell Stock II.


