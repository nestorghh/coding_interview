# they key idea to solve this problem is to think what the inverse of a fuction is
# easy

def decrypt(word):
  decrypted=''
  for i in range(len(word)):
    if i==0:
      decrypted = decrypted + chr(ord(word[i])-1)
    else:
      diff_prev = ord(word[i]) - ord(word[i-1])
      
      while not ord('a') <= diff_prev <= ord('z'):
        diff_prev+=26
        
      decrypted = decrypted + chr(diff_prev)
      
  return decrypted
