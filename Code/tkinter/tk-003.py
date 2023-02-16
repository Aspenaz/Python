""" Ventanas de aplicación y de diálogos 

Ventanas de aplicación se definen con Tk():
self.raiz = Tk()

Ventanas de diálogo (hijas) se definen con Toplevel():
self.dialogo = Toplevel() 



mainloop() (bucle principal) atiende eventos de la ventana de aplicación:
self.raiz.mainloop()

wait_window() atiende eventos de la ventana de diálogo mientras espera a ser cerrada:
self.raiz.wait_window(self.dialogo) """

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

class Aplicacion():
    ''' Clase Aplicacion '''

    ventana = 0
    posx_y = 0

    def __init__(self):
        ''' Construye ventana de aplicación '''
        self.raiz = Tk()
        self.raiz.geometry('300x210+500+50')  # Dimensión de la ventana 300x200 en la coordenada x=500, y=50.
        self.raiz.title("Ventana de aplicación")
        self.raiz.resizable(0,0)   

        self.text_info = Text (self.raiz, width=40, height=10, bg='beige' )   # , command=self.ver_info()

        separador_1 = ttk.Separator(self.raiz, orient=HORIZONTAL, takefocus=FALSE)   

        boton_abrir  = ttk.Button(self.raiz, text='Abrir', command=self.abrir )     
        boton_cerrar = ttk.Button(self.raiz, text='Cerrar', command=quit)
        
        self.text_info.pack(side=TOP, fill=NONE, padx=.5, pady=.5)
        separador_1.pack(side=TOP, fill=BOTH, padx=.5, pady=.5)
        boton_abrir.pack(side=LEFT, padx=5, pady=.5)
        boton_cerrar.pack(side=RIGHT, padx=5, pady=.5)

        boton_abrir.focus_set()

        self.raiz.mainloop()


    def abrir(self):
        ''' Construye una ventana de diálogo '''

        self.dialogo = Toplevel()

        Aplicacion.ventana+=1
        Aplicacion.posx_y += 50  

        tamypos = '250x100+' + str(Aplicacion.posx_y) + '+' + str(Aplicacion.posx_y)

        ident = self.dialogo.winfo_id()  # identicador de la nueva ventana
        titulo = str(Aplicacion.ventana) + ": " + str(ident)

        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0,0)
        self.dialogo.title(titulo)

        print('ventana:', Aplicacion.ventana)
        print('posx_y:', Aplicacion.posx_y)        
        print('tamypos:', tamypos)
        print('ident:', ident)
        print()

        boton_abrir = ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
        boton_abrir.pack(side=BOTTOM, padx=20, pady=20)
        boton_abrir.focus_set()

        self.ver_info()

        self.raiz.wait_window(self.dialogo)


    def ver_info(self):
        self.text_info.delete("1.0", END)

   
        info1 = str(self.dialogo.winfo_id())
        info2 = str(self.dialogo.winfo_geometry())
        info3 = str(Aplicacion.ventana)
        info4 = str(self.raiz.winfo_width())    
        info5 = str(Aplicacion.posx_y)   


        text_in = '\n'
        text_in += 'Id: ' + info1 + '\n' 
        text_in += 'Geometria: ' + info2 + '\n'
        text_in += 'N Ventana: ' + info3 + '\n'
        text_in += 'Anchura ventana: ' + info4 + '\n'
        text_in += 'Posx_y: ' + info5 + '\n' 

        # print()
        # print(text_in)
        # print('ventana:', Aplicacion.ventana)
        # print('posx_y:', Aplicacion.posx_y)        
        # print('tamypos:', tamypos)
        # print('ident:', ident)
        # print()

        self.text_info.insert('1.0', text_in)


def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()

