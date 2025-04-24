with open("fike.log","r") as f:
    fike = f.read()
with open("copyoffike.txt","r") as f:
    copy = f.read()
if fike == copy:
    print("both files are same")
else:
    print("both files are different")