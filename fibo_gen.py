def fibonacci_gen():
  f0, f1 = 0, 1
  
  while True:
    yield f1
    f0, f1 = f1, f0 + f1
