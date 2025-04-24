for i in range(2,21):
    with open(f'{i}.txt',"a+") as f:
        for z in range(1,21):
            f.write(str(i*z) + "\n")
