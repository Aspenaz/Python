def acelerar():
    
    global km  # Declara la variable 'km' como global
    
    tiempo1 = 1  # Declara variable local (ámbito función)
    global tiempo2
    tiempo2 = 1
    km+= 5

# Define variable local (ámbito programa principal)
km = 10

print('Velocidad:', km) 
acelerar()
print('Velocidad:', km) # 15
# print('Tiempo1:', tiempo1)  # NameError: name 'tiempo' is not defined
print('Tiempo2:', tiempo2)



print('\t\t\tscopes.py\n')

s = 0
for A in range(10):
    print('s:', s, 'A:', A, end='\t')
    s += A
    
print()
print('s:', s)
print('A:', A) 
# print('globals():', globals())
print()
# print('locals():', locals())
