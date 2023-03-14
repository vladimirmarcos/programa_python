import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu
from ventanas.creacion_frame import frame_inicio,frame_eliminar_credito,frame_busqueda_cuenta,frame_busqueda_dni,frame_mensajes,frame_informe_A,frame_informe_B,frame_pagos,frame_cuenta_nueva,frame_nuevo_credito,fram_enviar_a_judiciales

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)
        self.menu_inicio = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Crear",menu=self.menu_inicio)
        self.menu_inicio.add_command(label="Nuevo Credito",command=self.crear_frame_inicio)
        self.menu_inicio.add_command(label="eliminar Credito",command=self.crear_frame_eliminar)
        self.menu_inicio.add_command(label="Crear cuenta Nueva",command=self.crear_frame_nueva_cuenta)
        self.menu_inicio.add_command(label="Crear nuevo credito",command=self.crear_frame_nuevo_credito)
        self.menu_inicio.add_command(label="Enviar credito a Judiciales",command=self.enviar_credito_a_judiciales)
        
        self.menu_buscar = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Buscar", menu=self.menu_buscar)
        self.menu_buscar.add_command(label="Buscar por DNI",command=self.crear_frame_busqueda_dni)
        self.menu_buscar.add_command(label="Buscar por cuenta",command=self.crear_frame_busqueda_cuenta)
        parent.config(menu=self.menu)

        self.menu_pagos = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Pagos", menu=self.menu_pagos)
        self.menu_pagos.add_command(label="Pagos meses",command=self.crear_frame_pagos)
        parent.config(menu=self.menu)

        self.menu_mensajes = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Mensajes", menu=self.menu_mensajes)
        self.menu_mensajes.add_command(label="Mensajes",command=self.crear_frame_mensajes)
        parent.config(menu=self.menu)

        self.menu_informe = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Informe", menu=self.menu_informe)
        self.menu_informe.add_command(label="Informe A",command=self.crear_frame_informe_A)
        self.menu_informe.add_command(label="Informe B",command=self.crear_frame_informe_B)
        parent.config(menu=self.menu)
        self._frame = None

    def crear_frame_inicio(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None
        if self._frame is None:
            self._frame = frame_inicio(self)


    def crear_frame_nueva_cuenta(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None
        if self._frame is None:
            self._frame = frame_cuenta_nueva(self)

    def crear_frame_nuevo_credito(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None
        if self._frame is None:
            self._frame = frame_nuevo_credito(self)

    def crear_frame_eliminar(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None
        if self._frame is None:
            self._frame = frame_eliminar_credito(self)

    def enviar_credito_a_judiciales(self):
        if self._frame is not None:
            self._frame.borrar()
            self._frame = None
        if self._frame is None:
            self._frame = fram_enviar_a_judiciales(self)

    def crear_frame_busqueda_dni(self):
            if self._frame is not None:
                self._frame.borrar()
                self._frame = None
            if self._frame is None:
                self._frame = frame_busqueda_dni(self)


    def crear_frame_busqueda_cuenta(self):
            if self._frame is not None:
                self._frame.borrar()
                self._frame = None
            if self._frame is None:
                self._frame = frame_busqueda_cuenta(self)


    def crear_frame_pagos(self):
            if self._frame is not None:
                self._frame.borrar()
                self._frame = None
            if self._frame is None:
                self._frame = frame_pagos(self)



    def crear_frame_mensajes(self):
            if self._frame is not None:
                self._frame.borrar()
                self._frame = None
            if self._frame is None:
                self._frame = frame_mensajes(self)
    def crear_frame_informe_A(self):
            if self._frame is not None:
                self._frame.borrar()
                self._frame = None
            if self._frame is None:
                self._frame = frame_informe_A(self)


    def crear_frame_informe_B(self):
            if self._frame is not None:
                self._frame.borrar()
                self._frame = None
            if self._frame is None:
                self._frame = frame_informe_B(self)  

