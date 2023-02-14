""" Excepciones """

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================

""" try:
    numero = int(input("Introducir un número: "))
    factorial = 1
    for num in range(1, numero + 1):
        factorial *= num
    print(factorial)
except:
    print("Debe introducir un número entero") """
    

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================


try: 
    texto = input('Teclear :') 
except KeyboardInterrupt: 
    print('\nSe ha pulsado ctrl+c') 
else: 
    print('Ha tecleado {}'.format(texto)) 
finally: 
    print('fin de programa') 


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================