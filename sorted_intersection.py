
A=[1,2,2,4,7,9,10,10]
B=[0,6,7,9,10]

A=[1,1,2,2]
B=[2,2]

A=[2,3,3,5,5,6,7,7,8,12]
B=[5,5,6,8,8,9,10,10]

def intersection_sorted(A,B):
    m, n =len(A), len(B)
    a, b = 0, 0
    inter=[]
    
    while a<m and b<n:
        if A[a]==B[b]:
            if a==0 or A[a-1]!=A[a]:
                inter.append(A[a])
            a+=1
            b+=1
        
        elif A[a]<B[b]:
            a+=1
        else :
            b+=1
    return inter

print(intersection_sorted(A,B))



