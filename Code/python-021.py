""" Anotaciones de tipos: typing """



# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


repetir = 2
print(repetir)  # 2
print(type(repetir))  # class 'int'
print()

repetir = repetir * 'Typing'
print(repetir)  # TypingTyping
print(type(repetir))  # class 'str'
print()


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
# Variables y constantes


repetir: int = 3
cadena: str
cadena = repetir * 'Mundo'

print(repetir) 
print(cadena)

print()

print(__annotations__)

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
#  Tipo de argumentos en Funciones


def precio(entradas: int, festivo: bool=False) -> int:
    if festivo:
        return entradas * 10
    else:
        return entradas * 8

print('precio:', precio(3, True)) # 30
print('precio:', precio(4))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
# Tipo de argumentos en Clases


class Juego:
    tiempo: int = 40
    
    def __init__(self, nom: str, nivel: int, jug: int = 1) -> None:
        self.nom= nom
        self.nivel = nivel
        self.jug = jug
        
    def duracion(self) -> int:
        return self.jug * Juego.tiempo

partida = Juego('Ajedrez', 1, 2)
print('partida.duracion:', partida.duracion()) 
print(partida.nom, partida.nivel, partida.jug, partida.duracion(), partida.tiempo)
print(partida.__annotations__)
print(__annotations__)
print(partida.__class__)
print()
print(partida.__dict__)
print()
print(partida.__dir__())


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
# Anotaciones para tipos complejos

from typing import List, Dict, Set

apellidos: List[str] = ['Alcantara', 'Alonso', 'Blanco']
referencias: Dict[str, int] = {'Mesa': 121, 'Silla': 485}
serie: Set[int] = {1, 1, 1, 2, 2, 3, 3, 5, 5, 5, 5, 5, 6}


# def imprime_rios(rios: List[str]) -> None:  # return no devuelve nada por el -> None
#     for rio in rios:
#         return rio
def imprime_rios(rios: List[str]) -> None: 
    for rio in rios:
        print(rio)

imprime_rios(['Guadalquivir', 'Tinto', 'Odiel', 'Segura'])
print()
print('-Apellidos:'); imprime_rios(apellidos); print()
print('-Referencias:'); imprime_rios(referencias); print()
print('-Referencias.items():'); imprime_rios(referencias.items()); print()
print('-Referencias.keys():'); imprime_rios(referencias.keys()); print()
print('-Referencias.values():'); imprime_rios(referencias.values()); print()
print('-Serie:'); imprime_rios(serie)


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Alias

Los alias permiten la creación de anotaciones de tipo con denominaciones propias para mejorar
la comprensión del código. En el ejemplo siguiente se define el tipo Color como una tupla de tres
valores de tipo int para expresar la cantidad de rojo, verde y azul asociado a un determinado
color. Después, en la función pintar() se anota junto al argumento color el tipo Color que se
corresponde con dicha tupla: """

from typing import Tuple

Color = Tuple[int, int, int]

def pintar(color: Color) -> None:
    r: int
    v: int
    a: int
    r, v, a = color
    print('Color Rojo:', r, 'Verde:', v, 'Azul:', a)
    
pintar((100, 200, 120))
pintar((200, 300, 110))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Funciones con múltiples valores de retorno

Cuando una función devuelve múltiples valores el tipo del retorno se anota como una tupla con
los tipos de sus valores separados por comas, o por un tipo personalizado basado en la misma
construcción: Tuple[tipo, tipo, ...] """
 
from typing import Tuple

Coordenada = Tuple[int, int]

def coordenada_inicial() -> Coordenada:
    return 0, 0

print(coordenada_inicial())


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" 
Anotaciones para variables con valores de distinto tipo

Para variables que pueden tener valores de distinto tipo existen las anotaciones predefinidas
Optional y Union. Optional se utiliza con variables que pueden ser de un tipo concreto o de
ninguno (None). Y Union es apropiado para variables cuyos valores pueden ser de tipos
diferentes, excepto None.
En la función representantes() tanto el argumento votos como el valor de retorno son de tipo
Optional[int]. Por ello, tanto el valor del argumento votos como el que devuelve la función
pueden ser de tipo int o None. """

from typing import Optional

votos = Optional[int]
representantes = Optional[int]

def representantes(votos: votos) -> representantes:
    if votos:
        return votos // 5000
    else:
        return None
    
print(representantes(None)) # None
print(representantes(3409)) # 0
print(representantes(11231))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
from typing import Union

recuento = Union[str, float]

def recuento(inicio: bool, actual: int, final: int) -> recuento:
    if not inicio:
        return 'Escrutinio no iniciado'
    else:
        return round((actual * 100 / final), 2)
    
print(recuento(False, 0, 0)) # Escrutinio no iniciado
print(recuento(True, 4560, 9800))


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
# Mypy

from math import pi

def vol_esfera(radio: float) -> int:
    return round(4/3 * pi * radio ** 3, 2)

print(vol_esfera(2))

# $ pip install mypy
# $ mypy esfera.py
# typando1.py:4: error: Incompatible return value type (got "float", expected "int")
# Found 1 error in 1 file (checked 1 source file)

from math import pi

def vol_esfera(radio: float) -> float:  # el tipo del valor de retorno debe ser float
    return round(4/3 * pi * radio ** 3, 2)

print(vol_esfera(2))

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================