def canBePalindrome(s):
    from collections import defaultdict
    d=defaultdict(int)
    for c in s:
        d[c]+=1

    print(d)
    print([v%2 for v in d.values()])
    return sum( v%2 for v in d.values() )<=1


