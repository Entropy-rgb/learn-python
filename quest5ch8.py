def pattern(n):
    if n == 1:
        return "*"
    else:
        return("*"*n + "\n" +  pattern(n-1))
a = int(input('Enter Number : '))
print(pattern(a))
