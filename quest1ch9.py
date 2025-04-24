with open("poems.txt","r") as f:
    text = f.read()
text = text.lower()
if "twinkle" in text:
    print("The file poems.txt contains word \"twinke\".")
else:
    print('The file poems.txt doesn\'t contain the word \"twinkle\".')
