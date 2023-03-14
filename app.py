import tkinter as tk
from client.gui_app import App
from models.creditos_dao import actualizar_pagos
def main():
    ventana = tk.Tk()
    ventana.geometry("800x800")
    App(ventana).pack(side="top", fill="both", expand=True)
    ventana.mainloop()


if __name__=='__main__':
    actualizar_pagos()
    main()