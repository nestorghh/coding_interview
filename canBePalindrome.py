def canBePalindrome(s):
    from collections import defaultdict
    d=defaultdict(int)
    for c in s:
        d[c]+=1

    return sum( v%2 for v in d.values() )<=1


