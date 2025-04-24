three = "* * *"
two = "*   *"

a = int(input('Enter Number : '))
for i in range(1,a+1):
    if i%2 == 0:
        print(two)
    else:
        print(three)

