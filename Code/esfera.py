# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


from math import pi

def vol_esfera(radio: float) -> int:
    return round(4/3 * pi * radio ** 3, 2)

print(vol_esfera(2))
print(type(vol_esfera(2)))  # <class 'float'>

print()

# $ pip install mypy
# $ mypy esfera.py
# typando1.py:4: error: Incompatible return value type (got "float", expected "int")
# Found 1 error in 1 file (checked 1 source file)

from math import pi

def vol_esfera(radio: float) -> float:  # el tipo del valor de retorno debe ser float
    return round(4/3 * pi * radio ** 3, 2)

print(vol_esfera(2))
print(type(vol_esfera(2)))  # <class 'float'>


# $ mypy esfera.py
# Success: no issues found in 1 source file


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================