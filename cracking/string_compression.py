#string compression @cracking the coding interview.
























# this is not what is beaing asked.
from collections import Counter
def string_compression2(st):
	cs=''
	cnt = Counter()
	for c in st:
		cnt[c]+=1
	for k in cnt.keys():
		cs = cs+str(k)+str(cnt[k])
	return cs

print(string_compression('aabccccaaa'))
		
	




