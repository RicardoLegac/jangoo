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
        
        