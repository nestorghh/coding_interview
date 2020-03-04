#1221. Split a String in Balanced Strings

def balancedStringSplit(s):
    balancedCount = 0
    count = 0
    
    for i in s:
        if i == "L":
            count += 1
        
        if i == "R":
            count-=1

        if count == 0:
            balancedCount += 1

    return balancedCount



