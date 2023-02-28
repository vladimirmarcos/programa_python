from .conexion_db import ConexionDB
from tkinter import messagebox

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
	"monto"	REAL NOT NULL,
    "cuota"	INTEGER NOT NULL,
	"estado" INTEGER NOT NULL
);
    '''
    sql_1='''
     CREATE TABLE "fecha_vencimientos" (
	"fecha_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fecha"	TEXT NOT NULL,
	"monto_base"	REAL NOT NULL,
	"recargos"	REAL NOT NULL,
	"total"	REAL NOT NULL,
    "estado" INTEGER NOT NULL)
    ;
   '''



    try:
        conexion.cursor.execute(sql)
        conexion.cursor.execute(sql_1)
        #print("LLEGAMOS")
    except:
        pass

def borrar_tabla():
        conexion=ConexionDB()

        sql='DROP TABLE creditos'
        conexion.cursor.execute(sql)
        conexion.cerrar()

class Datos_Personas:
    def __init__(self,nombre,dni,garante,contacto,producto,monto,cuota,estado):
        self.id_cliente=None
        self.nombre=nombre
        self.dni=dni
        self.garante=garante
        self.contacto=contacto
        self.producto=producto
        self.monto=monto
        self.cuota=cuota
        self.estado=estado

    def __str__(self):
        return f'Creditos[{self.nombre},{self.dni},{self.garante},{self.contacto},{self.producto},{self.monto},{self.cuota},{self.estado}]'

class Fechas_Vencimiento:
    def __init__(self,fecha,monto_base,recargos,total,estado):
        self.id_fecha=None
        self.fecha=fecha
        self.monto_base=monto_base
        self.recargos=recargos
        self.total=total
        self.estado=estado
       

    def __str__(self):
        return f'Creditos[{self.fecha},{self.monto_base},{self.recargos},{self.total},{self.estado}]'

    
def guardar_datos_personas(Datos_Personas):
    conexion=ConexionDB()

    sql=f"""INSERT INTO datos_clientes (nombre,dni,garante,contacto,producto,monto,cuota,estado)
    VALUES ('{Datos_Personas.nombre}','{Datos_Personas.dni}','{Datos_Personas.garante}','{Datos_Personas.contacto}','{Datos_Personas.producto}','{Datos_Personas.monto}','{Datos_Personas.cuota}','{Datos_Personas.estado}')
    
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
    for fecha in range (numero+1): 
        sql=f"""INSERT INTO fecha_vencimientos (fecha,monto_base,recargos,total,estado)
        VALUES ('{Fechas_Vencimiento.fecha}','{Fechas_Vencimiento.monto_base}','{Fechas_Vencimiento.recargos}','{Fechas_Vencimiento.total}','{Fechas_Vencimiento.estado}')
    
        """
        conexion.cursor.execute(sql)
    conexion.cerrar()
        
def calcular_intereses(valor,cantidad):
    if (cantidad==1):
        return valor*1.13
    elif (cantidad==2):
        return valor*1.18
    elif (cantidad==3):
        return valor*1.23
    elif (cantidad==4):
        return valor*1.28
    elif (cantidad==5):
        return valor*1.33
    
