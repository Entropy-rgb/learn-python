b = ["sex","Donkey","fuck","hell"]
for item in b:
    with open("donkey.txt","r") as f:
        text = f.read()
        modified_text = text.replace(item,"#####")
    with open("donkey.txt","w") as a:
        a.write(modified_text)
