def find_nearest_repetition(paragraph):

    word_latest_index={}
    minDistance = float('Inf')

    for i, w in enumerate(paragraph):
        if w in word_latest_index:
            last_index_w = word_latest_index[w]
            minDistance= min(minDistance,i-last_index_w)

        word_latest_index[w]=i

    return minDistance

