import tkinter as tk



class MyFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.config(bg="blue")
        self.campos_creditos()


    def campos_creditos(self):
        #label de campos
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=0,padx=10,pady=10)

        self.label_garante=tk.Label(self,text='Garante')
        self.label_garante.config(font=('Arial',12,'bold'))
        self.label_garante.grid(row=2,column=0,padx=10,pady=10)

        self.label_contacto=tk.Label(self,text='contacto')
        self.label_contacto.config(font=('Arial',12,'bold'))
        self.label_contacto.grid(row=3,column=0,padx=10,pady=10)   

    def borrar(self):
        self.pack_forget()
        self.destroy()
        print("Frame borrado")


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)
        self.menu_buscar = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Crear",menu=self.menu_buscar)
        self.menu_buscar.add_command(label="Buscar_DNI",command=self.crear_frame)
        self.menu_buscar.add_command(label="Buscar_nombre",command=self.crear_frame)
        self.menu_notas = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Borrar", menu=self.menu_notas)
        self.menu_notas.add_command(label="Borrar frame",command=self.borrar_frame)
        parent.config(menu=self.menu)
        self._frame = None

    def crear_frame(self):
        if self._frame is None:
            self._frame = MyFrame(self)

    def borrar_frame(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("600x400")
    App(ventana).pack(side="top", fill="both", expand=True)
    ventana.mainloop()