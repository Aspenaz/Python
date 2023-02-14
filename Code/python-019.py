""" Iteradores y generadores """


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Recorrer los caracteres de una cadena: """

cadena = "Python"
for caracter in cadena:
    print(caracter)


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ==========================================================
""" Recorrer caracteres de cadena en sentido inverso. """

cadena = "Python"
for caracter in cadena[::-1]:
    print(caracter)
    
    
# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Recorrer los elementos de una lista """

lista = ['una', 'lista', 'es', 'un', 'iterable']
for palabra in lista:
    print(palabra)


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ==========================================================
""" Recorrer los elementos de la lista al revés """

lista = ['una', 'lista', 'es', 'un', 'iterable']
for palabra in lista[::-1]:
    print(palabra)


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Obtener índice para recorrer todos los elementos de la lista """

lista = ['una', 'lista', 'es', 'un', 'iterable']
for indice in range(len(lista)):
    print (indice, lista[indice])



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ==========================================================
""" Recorrer las claves de un diccionario """

artistas = { 'Lorca' : 'Escritor', 'Goya' : 'Pintor'}
for clave, valor in artistas.items():
    print(clave,':',valor)



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Leer las líneas de un archivo de texto, una a una """

for linea in open("datos.txt"):
    print(linea.rstrip())


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ==========================================================
""" La función iter() """

lista = [100, 1001, 10001, 100001]
iterador = iter(lista)
print(iterador)

try:
    while True:
        print(iterador.__next__())
except StopIteration:
    print("Se ha alcanzado el final de la lista")


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Implementando una clase para iterar cadenas """

# Clase para recorrer desde el último al primer caracter de una cadena de texto.

class Invertir:
    def __init__(self, cadena):
        self.cadena = cadena
        self.puntero = len(cadena)
        
    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.puntero == 0:
            raise(StopIteration)
        self.puntero = self.puntero - 1
        return(self.cadena[self.puntero])
    
    
cadena_invertida = Invertir('Iterable')
print(cadena_invertida)
iter(cadena_invertida)
print(cadena_invertida)

for caracter in cadena_invertida:
    print(caracter, end=' ')
 
print()   
# Devuelven caracteres que restan por iterar (ninguno):
print(list(cadena_invertida.__iter__()))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" La función range() """

for elemento in range(1, 11):
    print(elemento, end=' ')     # 1 2 3 4 5 6 7 8 9 10

print()    
for elemento in range(10, 0, -1):
    print(elemento, end=' ')     # 10 9 8 7 6 5 4 3 2 1

print()    
for elemento in range(0, 21, 5):
    print(elemento, end=' ')  


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ==========================================================
""" Generadores """

# una nueva llamada a un generador no inicia la ejecución al principio de la función, sino que la reanuda inmediatamente
# después del punto donde se encuentre la última declaración yield (que es donde terminó la función en la última llamada)
def gen_basico():
    yield "uno"
    yield "dos"
    yield "tres"
    
for valor in gen_basico():
    print(valor)



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
# Crea objeto generador y muestra tipo de objeto

generador = gen_basico()

print(generador) 
print(type(generador))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ==========================================================
# Convierte a lista el objeto generador y muestra elementos

lista = list(generador)

print(lista) # ['uno', 'dos', 'tres']
print(type(lista))

print()
print(list(gen_basico()))   # ['uno', 'dos', 'tres']


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

def gen_numeros(inicio):
    fin = inicio + 20
    while inicio < fin:
        yield inicio, fin
        inicio+=1
        
for inicio, fin in gen_numeros(20):
    print(inicio, fin)


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================
