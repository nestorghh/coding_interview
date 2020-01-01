#Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

def can3parts(A):

    suma = sum(A)

    if suma % 3 !=0:
        return False
    else:
        target = suma/3
        cumsum, count = 0,0

        for a in A:
            cumsum+=a

            if cumsum==target:
                count+=1
                cumsum=0
        return count==3

