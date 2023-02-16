
""" Pack

Lados de una ventana: arriba(TOP), abajo(BOTTOM), derecha(RIGHT) e izquierda(LEFT). """

# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================


from tkinter import *
from tkinter import ttk, font
import getpass

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        self.raiz.geometry('300x200')
        self.raiz.config(bg='beige')

        fuente = font.Font(weight='bold')  
        self.etiq1 = ttk.Label(self.raiz, text="Usuario:", font=fuente, foreground="green", background='beige')
        self.etiq2 = ttk.Label(self.raiz, text="Contraseña:", font=fuente, foreground="green", background='beige')
        
        self.usuario = StringVar()
        self.clave   = StringVar()
        
        self.usuario.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.usuario, width=30)
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=30, show="*")
        
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", command=quit)

        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

        self.ctext2.focus_set()
        
        self.raiz.mainloop()

    def aceptar(self):
        if self.clave.get() == 'tkinter':  # if self.ctext2.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario: ", self.ctext1.get())   # self.usuario.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()



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



# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================



