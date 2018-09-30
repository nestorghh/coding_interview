#longest common prefix

###############################################################
def longest_common_prefix(seq1, seq2):
    start = 0
    while start < min(len(seq1), len(seq2)):
        if seq1[start] != seq2[start]:
            break
        start += 1
    return seq1[:start]

seq1='geeksforgeeks'
seq2='carro'

print(longest_common_prefix(seq1,seq2))

#############################################################
#Longest Common Prefix | Set 1 (Word by Word Matching)
#Time complexity: O(N M)
# N: number of strings in the list
# M: length of the largest string in the list.
############################################################## 
def common_prefix(arr):
	prefix = arr[0]
	for i in range(1,len(arr)):
		prefix = longest_common_prefix(prefix,arr[i])
	return prefix

arr=['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(common_prefix(arr))
		
###############################################################
#Longest Common Prefix | Set 2 (Character by Character Matching)
#Time complexity : O(NM)
#Auxiliary space : O(M)

# A function to find the string having the minimum  length and 
# returns thre length
def findMinlength(arr):
	mini = len(arr[0])
	for i in range(0,len(arr)):
		if len(arr[i])<mini:
			mini = len(arr[i])
	return mini

arr=['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(findMinlength(arr))

# A function that returns the longest common prefix 
# from the array of strings

def commonPrefix_char(arr):
	minlen = findMinlength(arr)
	n = len(arr)
	result=''
	for i in range(0,minlen):
		current = arr[0][i]

		for j in range(1,n):
			if arr[j][i]!= current:
				return result
		result = result + current
	return result

arr=['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(commonPrefix_char(arr))

arr=['sdf', 'geeks', 'geek', 'geezer']
print(commonPrefix_char(arr))

##############################################################
# divide and conquer approach

def commonPrefix_dc(arr,low,high):
	
	if low==high:
		return arr[low]

	if (high > low):
		mid = (low+high)/2

		str1 = commonPrefix_dc(arr,low,mid)
		str2 = commonPrefix_dc(arr,mid+1,high)

		return longest_common_prefix(str1,str2)


arr=['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(commonPrefix_dc(arr,0,len(arr)-1))

arr=['abcd', 'abdre', 'abcree', 'abbvc']
print(commonPrefix_dc(arr,0,len(arr)-1))



#############################################################









