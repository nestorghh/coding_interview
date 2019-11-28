# find groups of anagrams using a hash table.
# computation consists of n calls to sort and n insertions into the hash table O(nmlogm)
# where m is the maximum string length.

def find_anagrams(words):

    from collections import defaultdict
    groups = defaultdict(list)

    for w in words:
        groups[''.join(sorted(w))].append(w)
        #groups[str(sorted(w))].append(w)

    return [group for group in groups.values() if len(group)>=2]


words=['debitcard','elvis','silent','badcredit','lives','freedom','listen','levis','money']

print(find_anagrams(words))


