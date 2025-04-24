
l = ["somesh","pawan","kamad","pooja","trisha","dada","dadi","radhe","khana"]

def remove_n_strip(a,l):
    c = a.strip()
    l.remove(c)
    return l
b = input('Enter Word: ') 
print(remove_n_strip(b,l))
