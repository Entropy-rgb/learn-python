import random
print('''
======================
    Welcome to the 
      Snake, 
      Water,
      Gun 
      Game
======================

''')
user = ""

while user != "d":
    b = random.randint(1,3)
    if b == 1:
        computer = "snake"
    elif b == 2:
        computer = "water"
    elif b == 3:
        computer = "gun"
    user = input('''
    Your Choice, enter
    a) Snake
    b) Water
    c) Gun
    d) exit game
    Enter Choice : ''')
    if user == "a" and computer == "water":
        print(f'You win, i chose {computer}')
    elif user == "b" and computer == "gun":
        print(f'You win, i chose {computer}')
    elif user == "c" and computer == "snake":
        print(f'You win, i chose {computer}')
    elif user == "d":
        exit()
    else:
        print(f'You Lose, i chose {computer}')
