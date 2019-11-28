def is_palindrome(s):

    i, j = 0, len(s)-1

    while i<j:

        while not s[i].isalnum() and i<j:
            i+=1

        while not s[j].isalnum() and i<j:
            j-=1

        if s[i].lower()!=s[j].lower():
            return False

        i+=1
        j-=1
    return True


print(is_palindrome('Able was I, ere I saw Elba!'))
print(is_palindrome('A man, a plan, a canal, Panama'))
print(is_palindrome('Ray a Ray'))

