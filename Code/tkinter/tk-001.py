# ===========================================================


# print('\n' + '=' * 94 + '\n')


# ===========================================================
""" 



from tkinter import * # interfaz Tkinter en versiones anteriores a la 8.5



from tkinter import ttk # para widgets nuevos 8.5+




raiz = Tk()



raiz.geometry('300x200')



raiz.configure(bg = 'beige')



raiz.title('Aplicación')




Button(raiz, text='Salir - widgets anteriores a la 8.5', command=quit).pack(side=BOTTOM)



ttk.Button(raiz, text='Salir - ttk widgets nuevos 8.5+', command=quit).pack(side=BOTTOM)





raiz.mainloop()

 """


# ===========================================================


# print('\n' + '=' * 94 + '\n')


# ===========================================================


# POO
""" 
from tkinter import *
from tkinter import ttk

class Aplicacion():

    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')     

        ttk.Button(raiz, text='Salir', command=raiz.destroy).pack(side=BOTTOM)    

        raiz.mainloop()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

 """


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================
# Obtener información

from tkinter import *
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("315x200")
        self.raiz.resizable(width=False, height=False)
        self.raiz.title("Ver info")

        self.t_info = Text(self.raiz, width=40, height=10, bg = 'beige')    

        self.b_info  = ttk.Button(self.raiz, text="Info", command=self.verinfo) 
        self.b_salir = ttk.Button(self.raiz, text="Salir", command=self.raiz.destroy)

        self.t_info.pack(side=TOP)
        self.b_info.pack(side=LEFT)
        self.b_salir.pack(side=RIGHT)

        self.b_info.focus_set()  # Sitúa el foco de la aplicación en el botón b_info

        self.raiz.mainloop()

    def verinfo(self):
        self.t_info.delete("1.0", END)  # def delete(index1: _TextIndex, index2: Optional[_TextIndex]=...) -> None

        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        # info7 = str(self.raiz.winfo_id())
        info7 = self.raiz.winfo_id()
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()

        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        # texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Id. de 'raiz': " + str(info7) + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n"
        texto_info += "Gestor ventanas: " + info9 + "\n"

        self.t_info.insert("1.0", texto_info)

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == "__main__":
    main()


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================
