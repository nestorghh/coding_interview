def binary_search(arr, var, s, f):
    midpoint = (s + f)//2
    if arr[midpoint] == var:
        return midpoint,arr[midpoint]
    elif arr[midpoint] < var and midpoint!=len(arr) and f <= len(arr):
        return binary_search(arr,var,midpoint,f+1)
    elif arr[midpoint] > var and midpoint!=0:
        return binary_search(arr, var, s, midpoint)
    else:
        print("not in the list")

lst=[0,0,0,0,0,1,1,1,1,1,1,1,1,1]
lst2 = [2,3,6,7,10,12,18]

#test binary search
binary_search(lst2,100,0,len(lst2)-1)



def binary_search2(arr, s, f):
    length = len(arr)
    midpoint = (s + f)//2
    #print('midpoint position is', midpoint)
    if arr[midpoint] == 1 and (arr[midpoint-1] == 0 or midpoint == 0):
        return length-midpoint
    elif arr[midpoint] == 1 and arr[midpoint-1] == 1:
        return binary_search2(arr,s,midpoint)
    elif arr[midpoint] ==  0 and midpoint != len(arr)-1:
        return binary_search2(arr, midpoint, f+1)
    else:
        return 0

def find_max_row(matrix):
    max = 0
    for i in range(len(matrix)):
        length_row=len(matrix[i])
        sum = binary_search2(matrix[i],0,length_row)
        #print(sum)
        if sum > max:
            max = sum
            winner = i
    print("The winner row is",winner)

#Tests:
#bin_list=[1,1,1,1]
#print(binary_search2(bin_list,0,len(bin_list)-1))

matrix = [[0,0,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1],[1,1,1,1,1],[0,0,0,0,0]]
find_max_row(matrix)



