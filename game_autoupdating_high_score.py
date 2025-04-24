def game():
    a = int(input('Enter a Number : '))
    return a
with open("Hi-score.txt","r") as f:
    c_high_score = f.read()
current_high_score = int(c_high_score)
b = game()
if  b > current_high_score:
    with open("Hi-score.txt","w") as c:
        c.write(str(b))
    print('New High Score',b)
else:
    print('Your High score was',c_high_score)
