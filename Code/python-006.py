""" Expresiones De Asignacion 


Las expresiones de asignación es una novedad que incorpora la sintaxis de Python 3.8 para
asignar valores a variables que son parte de una expresión, evitándose con ello el tener que
inicializarlas con antelación.
Para este tipo de asignación se utiliza dentro de la expresión el operador morsa := (walrus en
inglés)
"""
# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


print('Python para impacientes')

# inicializa
edad = 28
print(edad)

# inicializa y evalua inmediatamente
print(edad := 18)


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


def media(nota1, nota2):
    return (nota1 + nota2) / 2
'''
# ANTES: 
notafinal = media(6, 8)
if notafinal >= 5:
    print('Aprobado con:', notafinal)
'''
# AHORA:
# guarda el valor de una función en una variable y después se utiliza.
if (notafinal:=media(6, 8)) >= 5:
    print('Aprobado con', notafinal)
    
    
    
# ===========================================================    
print('\n' + '=' * 94 + '\n')
# ===========================================================  


'''
ANTES 
para hacer una asignación en un bucle se hacía dentro del mismo:
lista_compra = list()
while True:
    articulo = input('¿Qué necesitas comprar?: ')
    if articulo == '':
        print(lista_compra)
        break
    lista_compra.append(articulo)
'''
# AHORA 
# la misma asignación se puede hacer en la misma línea de while.
lista_compra = list()
while (articulo:=input('¿Qué necesitas comprar?: ')) != '':
    lista_compra.append(articulo)

print(lista_compra)



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================



# Las expresiones de asignación también se pueden utilizar en listas de comprensión:
parcelas_m2 = [220, 320, 180, 430]
precios = [(precio_m2 := 100) * sup for sup in parcelas_m2]
print(f'{precios} al precio de ${precio_m2} el m2')



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

""" El uso de paréntesis en las expresiones de asignación es fundamental para delimitar
exactamente el valor que se asigna a una variable: """


# a la variable 'precio' no se  asigna el valor 10, se asigna el resultado
# de comparar 10 y 5, es decir, True
if precio := 10 > 5:
    print(precio)

# En este caso queda más claro que es 10 el valor asignado a la variable precio
if (precio := 10) > 5:
    print(precio)


# Los paréntesis también permiten anidar expresiones para una asignación múltiple
(total := (precio := 10) * 5)
print(precio, total)



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

""" Diferencia básica entre el uso de = y := """


# asigna una tupla de 3 valores a la variable:
var1 = 0, 1, 2
print('var1:', var1)

# se asigna solo el primero de los valores: 0
(var1 := 0, 1, 2)
print('var1:', var1)

# lo recomendable es delimitar también por paréntesis los valores de la tupla
(var1 := (0, 1, 2))
print('var1:', var1)

# delimitar solo los valores de la tupla no es suficiente.
# var1 := (0, 1, 2)
print('var1:', var1)    # SyntaxError: invalid syntax


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================







# ===========================================================              
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94) 
# ===========================================================




# ===========================================================             
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================




# ===========================================================               
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================




# ===========================================================            
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================





# ===========================================================              
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================



# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================



# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================





# ===========================================================             
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94) 
# ===========================================================




# ===========================================================              
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================




# ===========================================================               
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================




# ===========================================================               
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')




# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================





# ===========================================================               
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# print('\t\t\tdata.py\n')




# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================


