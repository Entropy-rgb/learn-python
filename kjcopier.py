with open("fike.log","r") as f:
    text = f.read()

with open("copyoffike.txt","w") as f:
    f.write(text)