import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu

class frame_inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_creditos()
        
        #self.abrirventana2()

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

        
        self.label_producto=tk.Label(self,text='Producto')
        self.label_producto.config(font=('Arial',12,'bold'))
        self.label_producto.grid(row=4,column=0,padx=10,pady=10)

        self.label_cuotas=tk.Label(self,text='cuotas')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=5,column=0,padx=10,pady=10)

        self.label_monto=tk.Label(self,text='Monto')
        self.label_monto.config(font=('Arial',12,'bold'))
        self.label_monto.grid(row=6,column=0,padx=10,pady=10)

        #Entrys de cada Campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_garante=tk.StringVar()
        self.entry_garante=tk.Entry(self,textvariable=self.mi_garante)
        self.entry_garante.config(width=50,font=('Arial',12))
        self.entry_garante.grid(row=2,column=1,padx=10,pady=10,columnspan=2)


        self.mi_contacto=tk.StringVar()
        self.entry_contacto=tk.Entry(self,textvariable=self.mi_contacto)
        self.entry_contacto.config(width=50,font=('Arial',12))
        self.entry_contacto.grid(row=3,column=1,padx=10,pady=10,columnspan=2)


        self.mi_producto=tk.StringVar()
        self.entry_producto=tk.Entry(self,textvariable=self.mi_producto)
        self.entry_producto.config(width=50,font=('Arial',12))
        self.entry_producto.grid(row=4,column=1,padx=10,pady=10,columnspan=2)

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=5,column=1,padx=10,pady=10,columnspan=2)

        self.mi_monto=tk.StringVar()
        self.entry_monto=tk.Entry(self,textvariable=self.mi_monto)
        self.entry_monto.config(width=50,font=('Arial',12))
        self.entry_monto.grid(row=6,column=1,padx=10,pady=10,columnspan=2) 


         #botones

        self.boton_nuevo=tk.Button(self,text="Nuevo Credito")
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=7,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Generar",command="self.crear_frame_final_datos")
        self.boton_guardar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
        self.boton_guardar.grid(row=7,column=1,padx=10,pady=10)
        
        
        self._frame = None
        
    
    
   
    

    def borrar(self):
        self.pack_forget()
        self.destroy()
        



class frame_busqueda_dni(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_creditos_dni()

    def campos_creditos_dni(self):
        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=0,padx=10,pady=10)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        #botones

        self.boton_nuevo=tk.Button(self,text="Buscar ")
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)

    def borrar(self):
        self.pack_forget()
        self.destroy()


class frame_busqueda_nombre(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_creditos_nombre()

    def campos_creditos_nombre(self):
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

         #botones

        self.boton_nuevo=tk.Button(self,text="Buscar ")
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)

    def borrar(self):
        self.pack_forget()
        self.destroy()


class frame_pagos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_creditos_pagos()

    def campos_creditos_pagos(self):
        self.label_nombre=tk.Label(self,text='va algo para saber que cambio pagos')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        

    def borrar(self):
        self.pack_forget()
        self.destroy()

class frame_mensajes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_mensajes()

    def campos_mensajes(self):
        self.label_nombre=tk.Label(self,text='va algo para saber que cambio mensajes')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        

    def borrar(self):
        self.pack_forget()
        self.destroy()

class frame_informe_A(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_informe()

    def campos_informe(self):
        self.label_nombre=tk.Label(self,text='Fecha de inicio')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_nombre=tk.Label(self,text='Fecha de cierre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=1,column=0,padx=10,pady=10)

        #Entrys de cada Campo
        self.mi_fecha_inicio=tk.StringVar()
        self.entry_fecha_inicio=tk.Entry(self,textvariable=self.mi_fecha_inicio)
        self.entry_fecha_inicio.config(width=50,font=('Arial',12))
        self.entry_fecha_inicio.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_fecha_cierre=tk.StringVar()
        self.entry_fecha_cierre=tk.Entry(self,textvariable=self.mi_fecha_cierre)
        self.entry_fecha_cierre.config(width=50,font=('Arial',12))
        self.entry_fecha_cierre.grid(row=1,column=1,padx=10,pady=10,columnspan=2)



        #botones

        self.boton_nuevo=tk.Button(self,text="Generar ")
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)

    def borrar(self):
        self.pack_forget()
        self.destroy()

class frame_informe_B(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_informe()

    def campos_informe(self):
        self.label_nombre=tk.Label(self,text='Fecha de inicio')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_nombre=tk.Label(self,text='Fecha de cierre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=1,column=0,padx=10,pady=10)

        #Entrys de cada Campo
        self.mi_fecha_inicio=tk.StringVar()
        self.entry_fecha_inicio=tk.Entry(self,textvariable=self.mi_fecha_inicio)
        self.entry_fecha_inicio.config(width=50,font=('Arial',12))
        self.entry_fecha_inicio.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_fecha_cierre=tk.StringVar()
        self.entry_fecha_cierre=tk.Entry(self,textvariable=self.mi_fecha_cierre)
        self.entry_fecha_cierre.config(width=50,font=('Arial',12))
        self.entry_fecha_cierre.grid(row=1,column=1,padx=10,pady=10,columnspan=2)



        #botones

        self.boton_nuevo=tk.Button(self,text="Generar ")
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)
   

    def borrar(self):
        self.pack_forget()
        self.destroy()     


