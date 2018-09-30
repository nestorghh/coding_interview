#11. Container with most water.

#Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).  
#n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container and n is at least 2.

# https://www.geeksforgeeks.org/container-with-most-water/

##################################################################################
# O(n*n) solution
# O(1) space complexity

def maxArea(height):
	maxarea=0
	len_height=len(height)
	for i in range(0,len_height):
		for j in range(i+1,len_height):
			maxarea=max(maxarea,min(height[i],height[j])*(j-i))
	return maxarea


height= [1, 5, 4, 3]
print(maxArea(height))

height=[3, 1, 2, 4, 5]
print(maxArea(height))

####################################################################################
#Time complexity: O(n).
#Space complexity: O(1).

# cannot understand 100% why it is correct.

#Rationale: Initially we consider the area constituting the exterior most lines. Now, to maximize the area, 
#we need to consider the area between the lines of larger lengths. If we try to move the pointer at the 
#longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. 
#But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, 
#despite the reduction in the width. This is done since a relatively longer line obtained by moving 
#the shorter line's pointer might overcome the reduction in area caused by the width reduction.

def maxArea_efficient(height):
	maxarea=0
	left=0
	right=len(height)-1

	while left < right:
		area = (right - left) * min(height[left],height[right])
		maxarea = max(maxarea,area)
		
		if height[left] < height[right]:
			left=left+1
		else:
			right=right-1
	return maxarea
	
height= [1, 5, 4, 3]
print(maxArea_efficient(height))

height=[3, 1, 2, 4, 5]
print(maxArea_efficient(height))



