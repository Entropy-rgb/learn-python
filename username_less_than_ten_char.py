print('''

      Welcome to my app
''')
name = input('Enter your username : ')
if len(name) > 10:
    while len(name) > 10:
        print('Please enter a username less than 10 characters')
        name = input('Enter your username : ')
    print('Done')
else:
    print('Done')

print('Hi' , name)
