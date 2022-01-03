import tkinter as tk
from tkinter import font
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height=300)
   
   
    menu_inicio = tk.Menu(barra_menu,tearoff=0) #anclamos en barra de menu
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)
    menu_inicio.add_command(label='crear registro en la base de datos')
    menu_inicio.add_command(label='eliminar registro en la base de datos')
    menu_inicio.add_command(label='salir', command= root.destroy)
    
    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    menu_consultas.add_command(label='xd')

    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuraciones', menu = menu_configuracion)
    menu_configuracion.add_command(label='xd')

    menu_ayudas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayudas', menu = menu_ayudas)
    menu_ayudas.add_command(label='xd')


class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width=480, height=320)
        self.root = root
        self.pack()
        self.config( bg='grey')
        
        self.campos_peliculas()
        self.deshabilitar_campos()
        
    def campos_peliculas(self):
        #labels de cada campo
        self.label_nombre = tk.Label(self, text = 'Nombre')
        self.label_nombre.config(font=('Arial',12, 'bold'))
        self.label_nombre.grid(row = 0, column= 0, padx = 10, pady=10) #grid trabaja en filas y columnas como las tablas !
        
        self.label_duracion = tk.Label(self, text = 'Duracion')
        self.label_duracion.config(font=('Arial',12, 'bold'))
        self.label_duracion.grid(row = 1, column= 0, padx = 10, pady=10)

        self.self_genero = tk.Label(self, text = 'Genero')
        self.self_genero.config(font=('Arial',12, 'bold'))
        self.self_genero.grid(row = 2, column= 0, padx = 10, pady=10)
        
        #entrys de cada campo

        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, font= 'bold')
        self.entry_nombre.grid(row=0, column= 1,columnspan=2)

        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, font= 'bold')
        self.entry_duracion.grid(row=1, column= 1,columnspan=2)

        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, font= 'bold')
        self.entry_genero.grid(row=2, column= 1,columnspan=2)

        #botones

        self.boton_nuevo = tk.Button(self, text= 'Nuevo')
        self.boton_nuevo.config(width = 20, font = ('Arial', 12, 'bold'),
        fg= 'white' , bg='green', cursor='hand2', activebackground= '#35BD6F')
        self.boton_nuevo.grid(row=3, column=0,padx = 10, pady=10)

        self.boton_guardar = tk.Button(self, text= 'Guardar')
        self.boton_guardar.config(width = 20, font = ('Arial', 12, 'bold'),
        fg= 'white' , bg='blue', cursor='hand2', activebackground= '#35BD6F')
        self.boton_guardar.grid(row=3, column=1,padx = 10, pady=10)

        self.boton_cancelar = tk.Button(self, text= 'Cancelar')
        self.boton_cancelar.config(width = 20, font = ('Arial', 12, 'bold'),
        fg= 'white' , bg='red', cursor='hand2', activebackground= '#35BD6F')
        self.boton_cancelar.grid(row=3, column=2,padx = 10, pady=10)

    def hablitar_campos(self):
        pass

    def deshabilitar_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        self.boton_nuevo.config(state='disabled')
