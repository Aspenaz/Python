""" Salida Estándar: print() """

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

# Tabulando datos:

# Utilizando comodines:
# %s (cadena), %i (entero), %f (número con decimales)

# Los datos también se pueden tabular reservando un número determinado de caracteres:
# Ejemplo: 
# %10s reserva 10 posiciones y alinea a la izquierda
# %-10s reserva 10 posiciones y alinea a la derecha


personas = [('Claudio', 35, 1.826),
            ('Elena', 24, 1.84),
            ('Manuel', 90, 1.449),
            ('Isabel', 34, 1.72)]

for persona in personas:
    nombre = persona[0]
    edad = persona[1]
    altura = persona[2]
    print('%-8s tiene %2i años y mide %1.2f' % (nombre, edad, altura))
    
    
# Claudio  tiene 35 años y mide 1.83
# Elena    tiene 24 años y mide 1.84
# Manuel   tiene 90 años y mide 1.45
# Isabel   tiene 34 años y mide 1.72    




# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


lu = 'Quito (Ecuador)' 
la = -0.216979 
lo = -78.51627 

# concatena con formato de intérprete
# co = repr(lu)+': '+repr(la) + ',' + repr(lo)
ci = lu +': '+ str(la) + ',' + str(lo)
print(ci) # 'Quito (Ecuador)': -0.216979,-78.51627



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


val1 = 8.56767 
val2 = 9.45548 

# muestra redondeo con 2 y 3 decimales
print('{0:.3} : {1:.4}'.format(val1, val2))


print()


val1 = 89.56767 
val2 = 98.45548 

print('{0:.3} : {1:.4}'.format(val1, val2))
print('{0:.3f} : {1:.4f}'.format(val1, val2))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


# rellena con guiones bajos
print('{0:_^30}'.format('Capítulo'))
print()
# rellena con guiones medios
print('{0:-^30}'.format('Capítulo'))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

# rellena con ceros a la izquierda:

codpais = 593 

print(str(codpais).zfill(4))        # 0593
print(int(str(codpais).zfill(4)))   # 593
cod = str(codpais).zfill(4)
print(cod)                          # 0593
print(int(cod))                     # 593

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


valor = 3.141516 

print('Valor aprox. {0:.3f}'.format(valor)) # 3.142


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================



correos = {'SJK' : 300, 'LR': 309, 'B': 310}

for loc, cp in correos.items(): 
    # muestra lista de pares con formato
    print('{0:5}:{1:4d}'.format(loc, cp))

print()
    
for loc, cp in correos.items(): 
    print('{0:1}:{1:4}'.format(loc, cp))       # {índice:espacio}

print()
 
for loc, cp in correos.items(): 
    print('{0:2}:{1:4f}'.format(loc, cp))



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

    
print('Continuará...', end=' ') # ejecuta varios print() en misma...
print('otro día')               # ...línea.
    
    
# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

print('\nTabla de Multiplicar') 
for x in range(1, 11): # recorre los números del 1 al 10
    print(repr(x)+':') # imprime el nº de la tabla actual
    for y in range(1, 11): # recorre los números del 1 al 10
        print(repr(x).rjust(2).ljust(2), '*', end='') # muestra operadores y ...
        print(repr(y).rjust(3), end='') # … resultado en una línea
        print(' =' + repr(x*y).center(5))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


print('\nTabla de Multiplicar 2') 
for x in range(1, 11): # recorre los números del 1 al 10
    print(str(x)+':')  # imprime el nº de la tabla actual
    for y in range(1, 11): # recorre los números del 1 al 10
        print(str(x).ljust(2), '*', end='') # muestra operadores y ...
        print(str(y).rjust(3), end='') # … resultado en una línea
        print(' =' + str(x*y).center(5))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================



# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================