def sumn(n):
    if n == 0:
        a = 0
        return a
    else:
        a = n + sumn(n-1)
        return a
  
inp = int(input('enter number :'))
print(sumn(inp))
