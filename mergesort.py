import random
import time

#def merge(left,right):
#	if not left:
#		return right
#	
#	if not right:
#		return left
#	
#	if left[0] < right[0]:
#		return [left[0]] + merge(left[1:],right)
#	else:
#		return [right[0]] + merge(left, right[1:])


#def mergesort(lst):
#	if len(lst)<=1:
#		return lst
#	mid = len(lst)//2
#	left = mergesort(lst[:mid])
#	right = mergesort(lst[mid:])
#	return merge(left,right)

#lst=[44,38,2,13,98,34,12,1,29,0,22]

lst = random.sample(range(1000),1000)

#tick = time.time()
#print('Mergesort is O(nlogn)')
#print(mergesort(lst))
#print('Time to sort array was ', time.time() - tick)

def selectionsort(lst):

	for i in range(len(lst)):
		min_id = i
		for j in range(i+1,len(lst)):
			if lst[min_id] > lst[j]:
				min_id = j

		tmp = lst[min_id]
		lst[min_id] = lst[i]
		lst[i] = tmp

	return lst

tick = time.time()
print('Selectionsort is O(n²)')
selectionsort(lst)
print('Time to sort array was ', time.time() - tick)



def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


tick = time.time()
print('Mergesort is O(nlogn)')
merge_sort(lst)
print('Time to sort array was ', time.time() - tick)

tick = time.time()
print('Pythonsort is ????')
sorted(lst)
print('Time to sort array was ', time.time() - tick)















