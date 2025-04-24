def greatest(a,b,c):
    if a >= b and a >= c:
        print('greatest number is :',a)
    elif b >=a and b>=c:
        print('greatest number is :',b)
    elif c>=a and c>=b:
        print('greatest number is :',c)
    else:
        print('error')
a = int(input('Enter 1st number : '))
b = int(input('Enter 2nd number : '))
c = int(input('Enter 3rd number : '))
greatest(a,b,c)
