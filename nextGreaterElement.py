
def nextGreaterElement(nums1,nums2):
	result=[]
	for i in range(len(nums1)):
		found = False
		for j in range(len(nums2)):
			if found and nums2[j]>nums1[i]:
				result.append(nums2[j])
				break
			if nums1[i]==nums2[j]:
				found=True
			
			if (j==len(nums2)):
				result.append(-1)

	return result



