# given two lists, write a function that computes the differences (as in set difference), but taking into account duplicates.

def listDifference(A,B):
    from collections import defaultdict
    d = defaultdict(lambda:0)

    for a in A:
        d[a]+=1

    for b in B:
        d[b]-=1

    dres = []

    for k in d.keys():
        if d[k]!=0:
            dres.extend([k]*d[k])

    return dres

def listDifferences(A,B):
    return listDifference(A,B), listDifference(B,A)


