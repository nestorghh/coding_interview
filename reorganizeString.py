import heapq

def reorganizeString(s):
    pq = [(-s.count(x),x) for x in set(s)]
    heapq.heapify(pq)
    if any(-nc > (len(s)+1)/2 for nc, x in pq):
        return ""

    ans = []
    while len(pq) >= 2:
        print("maxheap ",pq)
        nct1, ch1 = heapq.heappop(pq)
        nct2, ch2 = heapq.heappop(pq)

        ans.extend([ch1,ch2])
        print("ans ",ans)

        print("nct1 + 1 ",nct1+1)
        print("nct2 + 1 ",nct2+1)

        if nct1 + 1: heapq.heappush(pq,(nct1 + 1, ch1))
        if nct2 + 1: heapq.heappush(pq,(nct2 + 1, ch2))

    return "".join(ans) + (pq[0][1] if pq else "")


