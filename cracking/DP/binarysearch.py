#not working 
#def binary_search(vector, val):
#        low = 0
#        upp = len(vector)-1

	#if vector[upp] < target:
	#	print('ELement not in array')
	#	return

#        while 1:
#                range = upp - low
#                if range==0 and vector[low]!=val:
#                        print('Element not in array')
#                        return
#                if vector[low]>vector[upp]:
#                        print('vector is not sorted')
#                        return
#                cent = ((range)//2) + low
#                if val == vector[cent]:
#                        return cent
#                elif val < vector[cent]:
#                        upp = cent - 1
#                else:
#                        low = cent + 1

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






