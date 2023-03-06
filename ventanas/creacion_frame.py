import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu
import datetime
from models.conexion_db import ConexionDB
from models.creditos_dao import Datos_Personas,guardar_datos_personas,Pagos,guardar_datos_fechas,Fechas_Vencimiento,crear_tabla,busquedadni,busquedanombre,pagos_cuotas,fin_credito
class frame_inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_creditos()
        self.desahabilitar_campos()
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


        self.label_monto=tk.Label(self,text='Monto')
        self.label_monto.config(font=('Arial',12,'bold'))
        self.label_monto.grid(row=5,column=0,padx=10,pady=10)

        self.label_cuotas=tk.Label(self,text='cuotas')
        self.label_cuotas.config(font=('Arial',12,'bold'))
        self.label_cuotas.grid(row=6,column=0,padx=10,pady=10)

       

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


        self.mi_monto=tk.StringVar()
        self.entry_monto=tk.Entry(self,textvariable=self.mi_monto)
        self.entry_monto.config(width=50,font=('Arial',12))
        self.entry_monto.grid(row=5,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        


         #botones

        self.boton_nuevo=tk.Button(self,text="Nuevo Credito",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=7,column=0,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="Generar",command=self.guardar_datos)
        self.boton_guardar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
        self.boton_guardar.grid(row=7,column=1,padx=10,pady=10)

        self.boton_guardar=tk.Button(self,text="tabla",command=crear_tabla)
        self.boton_guardar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
        self.boton_guardar.grid(row=7,column=2,padx=10,pady=10)
        
        
        self._frame = None

    def guardar_datos (self):
      try:
        nombre=self.mi_nombre.get()
        nombre=nombre.lower()
        nombre=nombre.strip()   
        garante=self.mi_garante.get() 
        garante=garante.lower()
        garante=garante.strip()
        contacto=self.mi_contacto.get()
        contacto=contacto.lower()
        contacto=contacto.strip()
        producto=self.mi_producto.get()
        producto=producto.lower()
        producto=producto.strip()
        monto=float(self.mi_monto.get())
        numero_cuota=int(self.mi_cuotas.get())
        total=self.calcular_intereses(monto,numero_cuota)
        dato_persona=Datos_Personas(
            nombre,
            self.mi_dni.get(),
            garante,
            contacto,
            producto,
            self.mi_monto.get(),
            total,
            self.mi_cuotas.get(),
            1
        )    
        
        guardar_datos_personas(dato_persona)
        fecha_actual=datetime.datetime.today()
        cuota=total/numero_cuota
        conexion=ConexionDB()
        sql=f"""SELECT max(id_clientes) FROM datos_clientes """
        conexion.cursor.execute(sql)
        algo=[]
        algo=conexion.cursor.fetchall()
        algo_1=algo[0]
        algo_2=list(algo_1)
        id_cliente=algo_2[0]
        conexion.cerrar()
        dato_fechas=Fechas_Vencimiento(
            fecha_actual,
            cuota,
            1,
            1,
            id_cliente
            


        )
        numero=int(self.mi_cuotas.get())
        guardar_datos_fechas(dato_fechas,numero)
        self.desahabilitar_campos()
      except:
        titulo=" error al registrar el pago"
        mensaje= "Verifique los campos, puede que falte alguno o que algun campo no fue llenado con su tipo valido" 
        messagebox.showerror(titulo,mensaje)

    def borrar(self):
        self.pack_forget()
        self.destroy()

    def habilitar_campos(self):
        

        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_garante.config(state='normal')
        self.entry_contacto.config(state='normal')
        self.entry_producto.config(state='normal')
        self.entry_cuotas.config(state='normal')
        self.entry_monto.config(state='normal')
        self.boton_guardar.config(state='normal')


    def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_garante.set('')
        self.mi_contacto.set('')
        self.mi_producto.set('')
        self.mi_cuotas.set('')
        self.mi_monto.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_garante.config(state='disabled')
        self.entry_contacto.config(state='disabled')
        self.entry_producto.config(state='disabled')
        self.entry_cuotas.config(state='disabled')
        self.entry_monto.config(state='disabled')

        self.boton_guardar.config(state='disabled')

    def calcular_intereses(self,valor,cantidad):
        if (cantidad==1):
            print(valor*1.13)
            return valor*1.13
        elif (cantidad==2):
            print(valor*1.18)
            return valor*1.18
        elif (cantidad==3):
            print(valor*1.23)
            return valor*1.23
        elif (cantidad==4):
            return valor*1.28
        elif (cantidad==5):
            return valor*1.33
          
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

        self.boton_nuevo=tk.Button(self,text="buscar",command=self.busqueda_dni)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)

    def borrar(self):
        self.pack_forget()
        self.destroy()

    

    def busqueda_dni(self):
        lista_clientes=[]
        dni=self.mi_dni.get()
        busquedadni(dni)
        self.mi_dni.set('')
        
        
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

        self.boton_nuevo=tk.Button(self,text="Buscar ",command=self.busqueda_nombre)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)

    def busqueda_nombre(self):
        lista_clientes=[]
        nombre=self.mi_nombre.get()
        
        
        nombre=nombre.lower()
        
        nombre=nombre.strip()
        busquedanombre(nombre)
        self.mi_nombre.set('')


    
        
        


    def borrar(self):
        self.pack_forget()
        self.destroy()


class frame_pagos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_creditos_pagos()

    def campos_creditos_pagos(self):
        

        #label de campos
        self.label_id=tk.Label(self,text='id del cliente')
        self.label_id.config(font=('Arial',12,'bold'))
        self.label_id.grid(row=0,column=0,padx=10,pady=10)



         #Entrys de cada Campo

        self.mi_id=tk.StringVar()
        self.entry_id=tk.Entry(self,textvariable=self.mi_id)
        self.entry_id.config(width=50,font=('Arial',12))
        self.entry_id.grid(row=0,column=1,padx=10,pady=10,columnspan=2)
       


          #botones

        self.boton_nuevo=tk.Button(self,text="Enviar",command=self.enviar_cuotas)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=7,column=0,padx=10,pady=10)
    def lista_vacia(self,lista):
        return not lista
    def prueba(self,ide):
        conexion=ConexionDB()
        sql=f"""SELECT fecha,monto_base,fecha_id FROM fecha_vencimientos WHERE idcliente='{ide}' AND estado=1"""
        conexion.cursor.execute(sql)
        algo=[]
        algo=conexion.cursor.fetchall()
        conexion.cerrar()
        return (algo)
    def enviar_cuotas(self):
        ide=self.mi_id.get()
        algo=self.prueba(ide)
        
        
        if (self.lista_vacia(algo)== False ):
            algo_1=algo[0]
            algo_2=list(algo_1)
            fecha=algo_2[0]
            monto=float(algo_2[1])
            fechaid=int(algo_2[2])
            fecha_actual=str(datetime.datetime.today())
        
            if (fecha<fecha_actual):
                monto=monto*1.13
                fecha_actual=datetime.datetime.today()
                pagare=Pagos(fecha_actual,monto,fechaid,int(ide))
                pagos_cuotas(pagare,fechaid)
           
            else:
                fecha_actual=datetime.datetime.today()
                ide=int(ide)
                pagare=Pagos(fecha_actual,monto,fechaid,ide)
                pagos_cuotas(pagare,fechaid)
            if (len(algo)-1==0):
                ide=int(ide)
                fin_credito(ide)
                   
                
            self.mi_id.set('')
            

        else:
            titulo=" error al registrar el pago"
            mensaje= "el cliente no registra más cuotas a pagar" 
            messagebox.showerror(titulo,mensaje)
            self.mi_id.set('')
            
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


