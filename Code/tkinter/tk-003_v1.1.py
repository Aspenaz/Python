""" Ventanas de aplicación y de diálogo: 

Ventanas de aplicación se definen con Tk(): self.raiz = Tk()

Ventanas de diálogo (hijas) se definen con Toplevel(): self.dialogo = Toplevel() 



mainloop() (bucle principal) 
Atiende eventos de la ventana de aplicación: self.raiz.mainloop()

wait_window() 
Atiende eventos de la ventana de diálogo mientras espera a ser cerrada: self.raiz.wait_window(self.dialogo) 
"""

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
        self.raiz.geometry('347x216+500+50') 
        self.raiz.title("Ventana de aplicación")
        self.raiz.resizable(0, 0) # type: ignore

        scrollbar = Scrollbar(self.raiz)  
        scrollbar.grid(row=0, column=2, padx=.1, sticky=(N, S)) # type: ignore 

        self.text_info = Text (self.raiz,  width=40, height=10, bg='beige' , yscrollcommand=scrollbar.set) 
        self.text_info.grid(row=0, column=0, columnspan=2, padx=2, pady=2, sticky=(E, W))  # type: ignore
        
        scrollbar.config(command=self.text_info.yview)  
        
        separador_1 = ttk.Separator(self.raiz, orient=HORIZONTAL)  
        separador_1.grid(row=1, column=0, columnspan=2, padx=5, pady=2, sticky=(E, W))  # type: ignore 
        
        boton_abrir  = ttk.Button(self.raiz, text='Abrir', command=self.abrir)  
        boton_abrir.grid(row=2, column=0, padx=20, pady=6)  
           
        boton_cerrar = ttk.Button(self.raiz, text='Cerrar', command=self.raiz.destroy) 
        boton_cerrar.grid(row=2, column=1, padx=20, pady=6)   
            

        boton_abrir.focus_set()

        self.raiz.mainloop()


    def abrir(self):
        ''' Construye una ventana de diálogo '''
        self.dialogo = Toplevel()

        Aplicacion.ventana+=1
        Aplicacion.posx_y += 50  

        self.tamypos = '250x100+' + str(Aplicacion.posx_y) + '+' + str(Aplicacion.posx_y)
        
        self.ident = self.dialogo.winfo_id()  
        
        titulo = str(Aplicacion.ventana) + ": " + str(self.ident)

        self.dialogo.geometry(self.tamypos)
        self.dialogo.resizable(0, 0)  # type: ignore
        self.dialogo.title(titulo)

        boton_cerrar_2 = ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)
        boton_cerrar_2.pack(side=BOTTOM, padx=20, pady=20)
        boton_cerrar_2.focus_set()

        self.ver_info()

        self.raiz.wait_window(self.dialogo)
    
    
    def ver_info(self):
        
        self.print()
        
        # self.text_info.delete("1.0", END)

        text_in = '\n'
        text_in += 'Ventana: '          + str(Aplicacion.ventana)   + '\n'      #todo 
        text_in += 'Id: '               + str(self.ident)           + '\n'      #todo 
        # text_in += 'Class: '            + self._class_dialogo       + '\n'   
        text_in += 'Geometria: '        + self.tamypos              + '\n'      #todo      
        # text_in += 'Anchura ventana: '  + str(self._width_dialogo)  + '\n'
        # text_in += 'Posx_y: '           + str(Aplicacion.posx_y)    + '\n' 
        # text_in += 'Altura ventana: '   + str(self._height_dialogo) + '\n' 
        text_in += 'Nombre: '           + self._name_dialogo        + '\n'      #todo 

        self.text_info.insert('1.0', text_in) 
           
        

    def print(self):
        self._class_dialogo         = self.dialogo.winfo_class()        #todo
        self._geometry_dialogo      = self.dialogo.winfo_geometry()     #todo
        self._width_dialogo         = self.dialogo.winfo_width()
        self._height_dialogo        = self.dialogo.winfo_height()
        self._rootx_dialogo         = self.dialogo.winfo_rootx()
        self._rooty_dialogo         = self.dialogo.winfo_rooty()
        self._name_dialogo          = self.dialogo.winfo_name()         #todo
        self._manager_dialogo       = self.dialogo.winfo_manager()
        self._vrootx_dialogo        = self.dialogo.winfo_vrootx()
        self._vrooty_dialogo        = self.dialogo.winfo_vrooty()
        self._server_dialogo        = self.dialogo.winfo_server()
        self._toplevel_dialogo      = self.dialogo.winfo_toplevel()
        self._screenvisual_dialogo  = self.dialogo.winfo_screenvisual()   

        print('ventana:', Aplicacion.ventana)
        print('posx_y:', Aplicacion.posx_y)        
        print('tamypos:', self.tamypos)
        print('ident:', self.ident)
        
        print('class:', self._class_dialogo)                    #todo      # Toplevel
        print('geometry:', self._geometry_dialogo)              #todo
        print('width:', self._width_dialogo)
        print('height:', self._height_dialogo)
        print('rootx:', self._rootx_dialogo)
        print('rooty:', self._rooty_dialogo)
        print('name:', self._name_dialogo)                      #todo
        print('manager:', self._manager_dialogo)
        print('vrootx:', self._vrootx_dialogo)
        print('vrooty:', self._vrooty_dialogo)
        print('server:', self._server_dialogo)
        print('toplevel:', self._toplevel_dialogo)
        print('screenvisual:', self._screenvisual_dialogo)
        print()


def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()
