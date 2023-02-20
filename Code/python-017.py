""" Funciones """


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones con un número fijo de parámetros """


def area_triangulo(base, altura): 
    ''' Calcular el área de un triangulo''' 
    return base * altura / 2 

print('area_triangulo:', area_triangulo(6, 4)) 
print('area_triangulo:', area_triangulo(3.5, 2.4))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones con un número variable de parámetros """


def distancia(*tramos): # define función con nº variable de parámetros
    ''' Suma distancia de tramos ''' 
    total = 0 
    for distancia in tramos: 
        total += distancia 
    return total 

tramo1 = 10
print(distancia(tramo1, 20, 30, 40)) 
print(distancia())


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones con parámetros con valores por defecto """


def pagar(importe, dto_aplicado = 5):
    ''' La función aplica descuentos '''
    return importe - (importe * dto_aplicado / 100)

print(pagar(1000)) # 950
print(pagar(1000, 10)) # 900


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Función con todos los parámetros con valores por defecto """


def repite_caracter(caracter="-", repite=3):
    return caracter * repite

print(repite_caracter()) # Se utilizan valores por omisión
print(repite_caracter('.',30)) # Muestra línea con 30 puntos
print(repite_caracter(repite=10, caracter='*'))



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones con parámetros que contienen diccionarios """


def porc_aprobados(aprobados, **aulas):
    ''' Calcula el % de aprobados '''
    total=0
    for alumnos in aulas.values():
        total += alumnos
        print(alumnos, 'aulas.values():', aulas.values())
    return aprobados * 100 / total

porcentaje_aprobados = porc_aprobados(48, A = 22, B = 25, C = 21)
print('{0:.2f}%'.format(porcentaje_aprobados))



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones que devuelven más de un valor """


def mineral(simbolo):
    ''' Devuelve número y denominación del mineral '''
    mineral = {'Au':'1-Oro', 'Hg':'2-Mercurio', 'Pt':'3-Plata'}
    elemento = mineral[simbolo]
    print(elemento)
    lista = elemento.split('-')
    return (lista[0], lista[1])

num, denomina = mineral('Au')
print('Número:', num)
print('Denominación:', denomina)



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones sin return """


def repite(caracter='-', repite=3):
    print(caracter * repite)   
     
repite('/', 94)



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones generadas a partir de otras """


at = area_triangulo # la función calcula área de un triángulo
print('area_triangulo:', at(10, 4))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================