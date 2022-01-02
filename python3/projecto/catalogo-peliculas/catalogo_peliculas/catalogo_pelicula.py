import tkinter as tk 
def main():
    root = tk.Tk()
    root.title('Majinbo')
    #root.iconbitmap('/majin.ico')
    root.resizable(0,0)
    
    
    #frame, contenedor de elementos

    frame = tk.Frame(root)
    frame.pack()
    frame.config(width=480, height=320, bg='grey')



    root.mainloop() #ejecuta el final de la ejecucion  

if __name__ == '__main__':
    main()