math = int(input('Enter marks scored in maths:'))
chem = int(input('Enter marks scored in chemistry:'))
phy = int(input('Enter marks scored in physics:'))
total = math + phy + chem
if total >= 40 and math > 32 and chem > 32 and phy > 32:
    print('Congratulation , you are Passed')
else:
    print('Work Hard, you failed')
    