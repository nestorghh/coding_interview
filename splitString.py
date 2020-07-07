def contains(s1,s2):

    set1 = set()
    set2 = set()

    for i in range(len(s1)):
        set1.add(s1[i])

    for i in range(len(s2)):
        set2.add(s2[i])

    return set1==set2


def splitWays(s):
    count=0
    for i in range(len(s)):
        s1 = s[0:i]
        s2 = s[i:len(s)]

        if contains(s1,s2):
            print('s1--->', s1)
            print('s2--->', s2)
            count+=1

    return count


