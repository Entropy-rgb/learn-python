marks = int(input('Enter Your Marks : '))

if marks in range(90,101):
    print('Grade : Ex')
elif marks in range(80,91):
    print('Grade : A')
elif marks in range(70,81):
    print('Grade : B')
elif marks in range(60,70):
    print('Grade : C')
elif marks in range(50,61):
    print('Grade : D')
else:
    print('Grade : F')
