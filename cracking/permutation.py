# Given two strings write a method to decide if one is a 
# permutation of the other.

def is_permutation(s1,s2):
	if len(s1)!=len(s2):
		return False
	if sorted(s1)==sorted(s2):
		return True
	else:
		return False

print(is_permutation('abc','acb'))
print(is_permutation('abc','zcb'))
print(is_permutation('abc','bca'))
print(is_permutation('cba','cab'))

# check if the two strings have identical character counts.
from collections import Counter #https://docs.python.org/2/library/collections.html

def is_permutation2(s1,s2):
	cnt = Counter()
	for i in s1:
		cnt[i] +=1
	for j in s2:
		cnt[j] -=1
	return not any(list(cnt.itervalues()))

print('================================')	
#print(is_permutation2('abcd','dcba'))		
print(is_permutation2('abc','acb'))
print(is_permutation2('abc','zcb'))
print(is_permutation2('abc','bca'))
print(is_permutation2('cba','cab'))


