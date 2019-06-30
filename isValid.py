class Solution(object):
	def isValid(self,s):
		#define a dictionary with all the brackets
		bdict = {'(':')','[':']','{':'}'}
		
		stack = []
		
		for bracket in s:
			if bracket in bdict:
				stack.append(bdict[bracket])
				print(stack)
			elif not stack or bracket != stack.pop():
				return False
		print('final stack', stack)
		return not stack


#a = Solution()

#a.isValid('()[]{}')

######################################################################

def isValid(s):
	bmap = {'(':')','[':']','{':'}'}
	stack=[]
	for bracket in s:
		if bracket in bmap:
			stack.append(bmap[bracket])
		elif bracket == stack.pop():
			continue
		else:
			return False
		print(stack)
	return not stack
			
			
print(isValid('()[]{}'))
print(isValid('()'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid('(]'))




