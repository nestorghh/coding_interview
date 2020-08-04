def root(x, n):
  
  y0=2
  tolerance = 0.001
  error = 10
  
  while (error>tolerance):
    y = y0 -(((y0**n)-x)*1.0/(n*y0**(n-1))) 
    print('y',y)
    error = abs(y-y0)
    print('err', error)
    y0 = y 
    print('y0',y0)
    
  return abs(y)
