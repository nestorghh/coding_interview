def binary_search(vector, val):
        low = 0
        upp = len(vector)-1

        while 1:
                range = upp - low
                if range==0 and vector[low]!=val:
                        print('Element not in array')
                        return
                if vector[low]>vector[upp]:
                        print('vector is not sorted')
                        return
                cent = ((range)/2) + low
                if val == vector[cent]:
                        return cent
                elif val < vector[cent]:
                        upp = cent - 1
                else:
                        low = cent + 1


print(binary_search([2,4,5,7,8,10],10))








