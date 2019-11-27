#Leetcode #121. Best Time to Buy and Sell Stock

def maxprofit_bf(prices):
	maxi=0
	for i in range(len(prices)-1):
		for j in range(i+1,len(prices)):
			margin = prices[j]-prices[i]
			if margin>maxi:
				maxi=margin

	return maxi


print(maxprofit_bf([7,1,5,3,6,4]))
print(maxprofit_bf([7,6,4,3,1]))


###############################################################

def maxprofit_linear(prices):
	mini=float('Inf')
	maxi=0
	for i in range(len(prices)):
		if prices[i]<mini:
			mini = prices[i]
		if (prices[i]-mini)>maxi:
			maxi = prices[i] - mini
	return maxi
	
	
print(maxprofit_linear([7,1,5,3,6,4]))
print(maxprofit_linear([7,6,4,3,1]))

#Runtime: 40 ms, faster than 87.92% of Python3 online submissions for Best Time to Buy and Sell Stock.

#Memory Usage: 13.7 MB, less than 97.41% of Python3 online submissions for Best Time to Buy and Sell Stock.

############################################################### 

def maxprofit_dp(prices):
	mini, maxi = float('Inf'), 0
	
	for i in range(len(prices)):
		mini = min(prices[i], mini)
		maxi = max(prices[i]-mini,maxi)
	return maxi

print(maxprofit_dp([7,1,5,3,6,4]))  
print(maxprofit_dp([7,6,4,3,1])) 

###############################################################

def max_profit_r(prices):
	maxi = 0
	min_price_sofar = float('Inf')

	for price in prices:
		 maxi_today = price - min_price_sofar
		 maxi = max (maxi_today,maxi)
		 min_price_sofar = min(min_price_sofar,price)
		 
	return maxi
			
print(max_profit_r([7,1,5,3,6,4]))
print(max_profit_r([7,6,4,3,1]))

