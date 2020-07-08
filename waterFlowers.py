def getRefills(flowers,c1,c2):

    refills=2
    n = len(flowers)
    i, j = 0, n-1
    cap1, cap2 = c1, c2

    while i!=j:

        if cap1>=flowers[i]:
            cap1-=flowers[i]
            i+=1
        else:
            cap1=5
            refills+=1
            cap1-=flowers[i]
            i+=1

        if cap2>=flowers[j]:
            cap2-=flowers[j]
            j-=1
        else:
            cap2=7
            refills+=1
            cap2-=flowers[j]
            j-=1


    if cap1+cap2<flowers[i]:
        cap1=5
        refills+=1

    return refills 





