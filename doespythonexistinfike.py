line_num = -1
found_lines = []
with open("fike.log","r") as f:
    for line_num, line in enumerate(f, 1):
        found_lines.append(line_num)
with open("fike.log","r") as f:
    text = f.read()
    lower = text.lower()
    
if "python" in lower:
    print("This file contains the word \"python\"")
else:
    pass
print(line_num)
