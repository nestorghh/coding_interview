# Given a number n, we need to find the sum of all the elements 
#from all possible subsets of a set formed by first n natural numbers

def sum_all_subsets(n):
	return ((n*(n+1)/2)*(2**(n-1))) # I have proved this by induction
	
# Induction step:

# The idea is that each time you add a new element (the element k+1), the previous sum
# (till element k) has to be considered twice plus (2^k) (k+1).

