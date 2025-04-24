a = int(input('Enter Number : '))
for i in range(1,a):
    if a%i:
        print('Number is composite')
        exit()
    else:
        print('Number is Prime')
        exit()