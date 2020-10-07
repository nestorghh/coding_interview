
def deletion_distance(str1, str2):
  n = len(str1)
  m = len(str2)
  
  if len(str1)==0:
    return len(str2)
  
  if len(str2)==0:
    return len(str1)
  
  
  if str1[n-1]!=str2[m-1]:
    return 1 + min(deletion_distance(str1[:n-1],str2), deletion_distance(str1,str2[:m-1]))
  
  if str1[n-1] == str2[m-1]:
    return deletion_distance(str1[:n-1],str2[:m-1])
