import string

b = input('Date :')
a = input('What is your good name:')
letter = '''
============================================          
           Dear User, 
           You are selected !              
           Date                            
============================================
            '''
mod1letter = letter.replace("User", a)
mod2letter = mod1letter.replace("Date", b)
print(mod2letter)
