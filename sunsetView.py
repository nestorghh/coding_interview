def sunsetView(buildings):

    candidates=[]

    for i in range(len(buildings)-1,-1,-1):

        while candidates and buildings[i]>=candidates[-1][1]:
            candidates.pop()
            #print(candidates)
        candidates.append((i,buildings[i]))
        #print(candidates)

    return [c for c in reversed(candidates)]





