def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


##############################################################################
def binarySearch(arr, x): 
	l =0
	r = len(arr)-1

	while l <= r: 

        	mid = l + (r - l)//2; 
          
        	# Check if x is present at mid 
        	if arr[mid] == x: 
            		return mid 
  
        	# If x is greater, ignore left half 
        	elif arr[mid] < x: 
            		l = mid + 1
  
        	# If x is smaller, ignore right half 
        	else: 
            		r = mid - 1
      
   	 # If we reach here, then the element 
    	# was not present 
	return False


#print(binary_search([2,4,5,7,8,10],7))

#print(binary_search([10,11,16,20],12))






