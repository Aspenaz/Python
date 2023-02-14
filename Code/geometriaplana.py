'''Funciones de geometría plana
Para el cálculo del área de las siguientes figuras:
'''

from math import pi

def area_cuadrado(lado):
    '''Función area_cuadrado: Calcula área de un cuadrado.
    area_cuadrado = lado ** 2 '''
    return (lado ** 2)

def area_rectangulo(base, altura):
    '''Función area_rectangulo: Calcula área de un rectángulo.
    area_rectangulo = base * altura '''
    return (base * altura)

def area_triangulo(base, altura):
    '''Función area_triangulo: Calcula área de un triángulo.
    area_triangulo = base * altura / 2 '''
    return (base * altura / 2)

def area_paralelogramo(base, altura):
    '''Función area_paralelogramo: Calcula área de un paralelogramo.
    area_paralelogramo = base * altura '''
    return (base * altura)

def area_trapecio(baseMayor, baseMenor, altura):
    '''Función area_trapecio: Calcula área de un trapecio.
    area_trapecio = (baseMayor + baseMenor) * altura / 2'''
    return (baseMayor + baseMenor) * altura / 2

def area_circulo(radio):
    '''Función area_circulo: Calcula área de un circulo.
    area_ciruculo = pi * radio ** 2 '''
    return (pi * radio ** 2)


# $ python -m pydoc -k geometria
# geometriaplana

# $ python -m pydoc geometriaplana 

# $ python -m pydoc -w geometriaplana

# $ python -m pydoc -p 8080      
# Server ready at http://localhost:8080/
