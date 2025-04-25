total = 0
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(1,33):
    if fibonacci(i)%2 == 0 and fibonacci(i) <= 4000000:
        total = total + fibonacci(i)
    else:
        pass
print(total)
