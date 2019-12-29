#leetcode 1071
#For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

#Return the largest string X such that X divides str1 and X divides str2.

def gcdOfStrings(str1,str2):
    import math
    
    gcd = math.gcd(len(str1),len(str2))
    sgcd=""

    for i in range(gcd):
        if str1[i]!=str2[i]:
            break
        else:
            sgcd+=str1[i]

    m, n = len(str1)//gcd, len(str2)//gcd

    if str1==sgcd*m and str2==sgcd*n:
        return sgcd
    else:
        return ""

