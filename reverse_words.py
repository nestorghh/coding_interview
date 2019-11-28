def reverse_words(s):

    def reverse_indiv(s,start,finish):
        while start<finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start+1, finish-1

    # remove the whole thing

    reverse_indiv(s,0,len(s)-1)

    start=0

    while True:
        finish=start

        while finish < len(s) and s[finish]!=' ':
            finish+=1

        if finish == len(s):
            break

        reverse_indiv(s,start,finish-1)
        start=finish+1

    # reverse the last word

    reverse_indiv(s,start,len(s)-1)
    
    return s
