a = int(input('Enter Number which you want Factorial of : '))  #n
b = 1 # rth term
if a >= 0 :
    for i in range(1,a+1):
        b = b*i
    print(f'The Factorial of {a} is {b}')
else:
    print('Factorial of a negative integer is not defined')

