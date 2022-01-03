import tkinter as tk 
from client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title('Majinbo')
    #root.iconbitmap('/majin.ico')
    root.resizable(0,0)
    
    barra_menu(root)
    app = Frame(root = root)
    
    #frame, contenedor de elementos

    '''
    todo esto se fue dentro de gui_app.py que es el entorno grafico de la app. todo lo que sea del frame 
    '''
    



    app.mainloop() #ejecuta el final de la ejecucion  

if __name__ == '__main__':
    main()