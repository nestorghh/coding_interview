#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1,w2=-1,-1
        mind = float('Inf')
        for i, w in enumerate(words):
            if w==word1:
                w1=i
            if w==word2:
                w2=i
            if w1!=-1 and w2!=-1:
                mind = min(mind,abs(w2-w1))
                
        return mind
