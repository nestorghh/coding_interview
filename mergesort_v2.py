def merge_two_sorted(a,b):

	sorted_list = []
	l=0
	r=0
	while l < len(a) and r < len(b):
		if a[l]<=b[r]:
			sorted_list.append(a[l])
			l+=1
		elif a[l]>b[r]:
			sorted_list.append(b[r])
			r+=1
	
	if r!=(len(b)-1):
		sorted_list+=a[l:]		
	
	if l!=(len(a)-1):
		sorted_list+=b[r:]

	return sorted_list

a=[8,12,21,30]
b=[1,6,7,9]

print(merge_two_sorted(a,b))


def mergesort(c):
	if len(c)==1:
		return c

	m = (len(c))//2
	
	a = mergesort(c[:m])
	b = mergesort(c[m:len(c)])

	return merge_two_sorted(a,b)
	
	

c=[200,54,1,23,54,22,-34,-1,2343]
print(mergesort(c))

