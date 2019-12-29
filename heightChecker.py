#leetcode 1051

#Students are asked to stand in non-decreasing order of heights for an annual photo.
#Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

#Idea: sort heights and then check with original for discrepancies.


def heightChecker(heights):
    b=sorted(heights)

    return len([i==j for i,j in zip(heights,b) if (i==j)==False])
    
