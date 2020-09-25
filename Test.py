def sumnumbers(x):
    if x == 1:
      return 1
    else:
      return x+sumnumbers(x-1)

print(sumnumbers(9))
