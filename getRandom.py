def get_random_from(intervals):
    import random
    upper = 0

    for inter in intervals:
        upper += (inter[1]-inter[0])+1

    randint = random.randint(1,upper)
    print(randint)

    for inter in intervals:
        currentRange = inter[1]-inter[0]+1

        if randint<=currentRange:
            result = inter[0]+randint-1
            break
        else:
            randint-=currentRange

    return result



