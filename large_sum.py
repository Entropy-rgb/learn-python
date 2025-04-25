summ = 0
with open('numbers.txt',"r") as f:
    text = f.readlines()
    for line in text:
        summ = summ + int(line)

print(summ)