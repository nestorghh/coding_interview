#Return the index of the first occurrence of needle in haystack, 
#or -1 if needle is not part of haystack.
################################################################
def strStr(haystack,needle):
        len_n = len(needle)
        len_hay = len(haystack)

        if len(needle)==0:
                return 0

        for i in range(0,len_hay-len_n+1):
                if haystack[i:i+len_n]==needle:
                        return i
        return -1
###############################################################

haystack = "hello"
needle = "ll"
print(strStr(haystack,needle))

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack,needle))

haystack='a'
needle='a'
print(strStr(haystack,needle))


