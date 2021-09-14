
def rotationalCipher(input, rotation_factor):
  # Write your code here
  
  new_string=[]
  
  if not input or not rotation_factor:
    return input
  
  cap_alpha = [chr(c) for c in range(ord("A"),ord("Z")+1)]
  alpha = [chr(c) for c in range(ord("a"),ord("z")+1)]
 
  for c in input:
    
    if not c.isalnum():
      
      new_string.append(c)
      
    elif c.isalpha():
      
      if c.isupper():
        
        idx = cap_alpha.index(c) + rotation_factor
        
        if idx>25:
          
          idx %=26
        
        new_string.append(cap_alpha[idx])
      else:
        
        idx = alpha.index(c) + rotation_factor
        
        if idx>25:
          idx%=26
          
        new_string.append(alpha[idx])
        
    elif c.isdigit():
      new_string.append(str(int(c)+rotation_factor)[-1])

  return ''.join(new_string)
