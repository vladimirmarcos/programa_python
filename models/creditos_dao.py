from .conexion_db import ConexionDB
from tkinter import messagebox
import datetime
def crear_tabla():
    conexion=ConexionDB()
    
    sql='''
    CREATE TABLE "datos_clientes" (
	"id_clientes"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nombre"	TEXT NOT NULL,
	"dni"	TEXT NOT NULL,
	"garante"	TEXT NOT NULL,
	"contacto"	TEXT NOT NULL,
	"producto"	TEXT NOT NULL,
	"monto_s"	REAL NOT NULL,
    "monto_c"	REAL NOT NULL,
    "cuota"	INTEGER NOT NULL,
	"estado" INTEGER NOT NULL
);
    '''
    sql_1='''
     CREATE TABLE "fecha_vencimientos" (
	"fecha_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fecha"	TEXT NOT NULL,
	"monto_base"	REAL NOT NULL,
    "estado" INTEGER NOT NULL,
    "al_dia" INTEGER NOT NULL,
    "idcliente" INTEGER NOT NULL)
    ;
   '''

    sql_2='''
     CREATE TABLE "pagos" (
	"pagos_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fecha_pago"	TEXT NOT NULL,
	"monto_pagado"	REAL NOT NULL,
    "fecha_id" INTEGER NOT NULL,
    "id_cliente" INTEGER NOT NULL)
    ;
   '''

    try:
        conexion.cursor.execute(sql)
        conexion.cursor.execute(sql_1)
        conexion.cursor.execute(sql_2)
        #print("LLEGAMOS")
    except:
        pass

def borrar_tabla():
        conexion=ConexionDB()

        sql='DROP TABLE creditos'
        conexion.cursor.execute(sql)
        conexion.cerrar()

class Datos_Personas:
    def __init__(self,nombre,dni,garante,contacto,producto,monto_s,monto_c,cuota,estado):
        self.id_cliente=None
        self.nombre=nombre
        self.dni=dni
        self.garante=garante
        self.contacto=contacto
        self.producto=producto
        self.monto_s=monto_s
        self.monto_c=monto_c
        self.cuota=cuota
        self.estado=estado

    def __str__(self):
        return f'Creditos[{self.nombre},{self.dni},{self.garante},{self.contacto},{self.producto},{self.monto_s},{self.monto_c},{self.cuota},{self.estado}]'

class Fechas_Vencimiento:
    def __init__(self,fecha,monto,estado,al_dia,idcliente):
        self.id_fecha=None
        self.fecha=fecha
        self.monto=monto
        self.estado=estado
        self.al_dia=al_dia
        self.idcliente=idcliente
       

    def __str__(self):
        return f'Creditos[{self.fecha},{self.monto},{self.estado},{self.al_dia},{self.idcliente}]'

class Pagos:   
    def __init__(self,fecha_pago,monto_pagado,fecha_id,id_cliente):
        self.pagos_id=None
        self.fecha_pago=fecha_pago
        self.monto_pagado=monto_pagado
        self.fecha_id=fecha_id
        self.id_cliente=id_cliente

    def __str__(self):
        return f'Creditos[{self.fecha_pago},{self.monto_pagado},{self.estado},{self.fecha_id},{self.id_cliente}]'


def guardar_datos_personas(Datos_Personas):
    conexion=ConexionDB()

    sql=f"""INSERT INTO datos_clientes (nombre,dni,garante,contacto,producto,monto_s,monto_c,cuota,estado)
    VALUES ('{Datos_Personas.nombre}','{Datos_Personas.dni}','{Datos_Personas.garante}','{Datos_Personas.contacto}','{Datos_Personas.producto}','{Datos_Personas.monto_s}','{Datos_Personas.monto_c}','{Datos_Personas.cuota}','{Datos_Personas.estado}')
    
    """
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
    except:
        titulo=" error al registrar el credito"
        mensaje= "Verifique los campos, puede que falte alguno o que algun campo no fue llenado con su tipo valido"
        messagebox.showerror(titulo,mensaje)

 

def guardar_datos_fechas(Fechas_Vencimiento,numero):
    conexion=ConexionDB()
    dia_delta=datetime.timedelta(days=31)
    Fechas_Vencimiento.fecha= Fechas_Vencimiento.fecha+dia_delta
    sql=f"""INSERT INTO fecha_vencimientos (fecha,monto_base,estado,al_dia,idcliente)
        VALUES ('{Fechas_Vencimiento.fecha}','{Fechas_Vencimiento.monto}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.al_dia}','{Fechas_Vencimiento.idcliente}')
    
        """
    conexion.cursor.execute(sql)
    for fecha in range (numero-1): 
        Fechas_Vencimiento.fecha= Fechas_Vencimiento.fecha+dia_delta
        sql=f"""INSERT INTO fecha_vencimientos (fecha,monto_base,estado,al_dia,idcliente)
        VALUES ('{Fechas_Vencimiento.fecha}','{Fechas_Vencimiento.monto}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.al_dia}','{Fechas_Vencimiento.idcliente}')
    
        """
        conexion.cursor.execute(sql)
    conexion.cerrar()
def pagos_cuotas(Pagos):
    conexion=ConexionDB()

    sql=f"""INSERT INTO pagos (fecha_pago,monto_pagado,fecha_id,id_cliente)
    VALUES ('{Pagos.fecha_pago}','{Pagos.monto_pagado}','{Pagos.fecha_id}','{Pagos.id_cliente}')
    
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        
    except:
      titulo=" error al registrar el pago"
      mensaje= "Verifique los campos, puede que falte alguno o que algun campo no fue llenado con su tipo valido"
      messagebox.showerror(titulo,mensaje)
    

def busquedadni(dni):
    conexion=ConexionDB()
    lista_vacia=[]
    sql=f""" SELECT id_clientes,nombre, producto FROM datos_clientes WHERE dni='{dni}'"""
    conexion.cursor.execute(sql)
    lista_vacia=conexion.cursor.fetchall()
    algo=lista_vacia[(0)]
    
    print(lista_vacia[(0)])
    
    #print(lista_vacia(0))
    conexion.cerrar()
    



def busquedanombre(nombre):
    conexion=ConexionDB()
    lista_vacia=[]
    sql=f""" SELECT id_clientes,nombre, producto FROM datos_clientes WHERE nombre='{nombre}'
    """
    conexion.cursor.execute(sql)
    lista_vacia=conexion.cursor.fetchall()
    conexion.cerrar()
    print(lista_vacia)