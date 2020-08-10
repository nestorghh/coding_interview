def bracket_match(text):
  #pass # your code goes here
  
  count, stack = 0, []
  
  for char in text:
    if char=="(":
      stack.append(char)
    elif char==")":
      if stack==[]:
        count+=1
      elif stack[-1]=='(':
        stack.pop()
  
  return count+len(stack) 
