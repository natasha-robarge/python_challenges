def fib(x):
  # Your code here
  prev = 0
  nex = 1
  for nex in range(0, x):
    num = prev
    prev = nex
    nex = num + prev
  print(nex)

fib(2)
