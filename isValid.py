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
	#bmap = {'(':')','[':']','{':'}'}
	bmap={")": "(", "}": "{", "]": "["}
	stack=[]
	for bracket in s:
		if bracket in bmap:
			top = stack.pop() if stack else '#'
			if bmap[bracket]!=top:
				return False
		else:
			stack.append(bracket)
	return not stack
		
			
print(isValid('()[]{}'))
print(isValid('()'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid('(]'))




