from .conexion_db import ConexionDB
from tkinter import messagebox
import datetime
def crear_tabla():
    conexion=ConexionDB()
    sql="""
    CREATE TABLE "cuentas" (
	"id_cuenta"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"nombre"	TEXT NOT NULL,
	"dni"	INTEGER NOT NULL UNIQUE,
	"contacto_telefono"	TEXT NOT NULL,
	"contacto_direccion"	TEXT NOT NULL,
	"calificacion"	TEXT NOT NULL
);

"""
    sql_1="""
  CREATE TABLE "creditos" (
	"credito"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"cuenta"	INTEGER NOT NULL,
	"cuotas"	INTEGER NOT NULL,
	"productos"	TEXT NOT NULL,
	"monto_base"	REAL NOT NULL,
	"telefono_garante"	TEXT NOT NULL,
	"direccion_garante"	TEXT NOT NULL,
	"judiciales"	INTEGER NOT NULL,
	"estado"	INTEGER NOT NULL
);
  """

   
    sql_2='''
     CREATE TABLE "fechas_pagos" (
	"fecha_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"fecha"	TEXT NOT NULL,
	"monto_base"	REAL NOT NULL,
	"estado"	INTEGER NOT NULL,
	"al_dia"	INTEGER NOT NULL,
	"cuenta"	INTEGER NOT NULL,
	"credito"	INTEGER NOT NULL
);
   '''

    sql_3='''
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
        conexion.cerrar()
        
    except:
        pass

def borrar_tabla():
        conexion=ConexionDB()

        sql='DROP TABLE creditos'
        conexion.cursor.execute(sql)
        conexion.cerrar()

class Datos_Personas:
    def __init__(self,nombre,dni,contacto_telefono,contacto_dirreccion,calificacion):
        self.id_cliente=None
        self.nombre=nombre
        self.dni=dni
        self.contacto_telefono=contacto_telefono
        self.contacto_direccion=contacto_dirreccion
        self.calificacion=calificacion
       

    def __str__(self):
        return f'Creditos[{self.nombre},{self.dni},{self.contacto_telefono},{self.contacto_direccion},{self.calificacion}]'


class Cuentas_Personas:
     def __init__(self,nombre,dni,contacto_telefono,contacto_dirreccion,calificacion):
        self.id_cliente=None
        self.nombre=nombre
        self.dni=dni
        self.contacto_telefono=contacto_telefono
        self.contacto_direccion=contacto_dirreccion
        self.calificacion=calificacion
       

     def __str__(self):
        return f'Creditos[{self.nombre},{self.dni},{self.contacto_telefono},{self.contacto_direccion},{self.calificacion}]'


class Creditos:
     def __init__(self,cuenta,cuotas,productos,monto_base,telefono_garante,direccion_garante,judiciales,estado):
        self.credito=None
        self.cuenta=cuenta
        self.cuotas=cuotas
        self.productos=productos
        self.monto_base=monto_base
        self.telefono_garante=telefono_garante
        self.direccion_garante=direccion_garante
        self.judiciales=judiciales
        self.estado=estado
       

     def __str__(self):
        return f'Creditos[{self.cuenta},{self.cuotas},{self.productos},{self.monto_base},{self.telefono_garante},{self.direccion_garante},{self.judiciales},{self.estado}]'

class Fechas_Vencimiento:
    def __init__(self,fecha,monto_base,estado,al_dia,cuenta,credito):
        self.id_fecha=None
        self.fecha=fecha
        self.monto_base=monto_base
        self.estado=estado
        self.al_dia=al_dia
        self.cuenta=cuenta
        self.credito=credito
       

    def __str__(self):
        return f'Creditos[{self.fecha},{self.monto_base},{self.estado},{self.al_dia},{self.cuenta},{self.credito}]'

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


def buscar_cuenta(cuenta):
    conexion=ConexionDB()
    
        
    sql=f""" SELECT id_cuenta FROM cuentas WHERE id_cuenta='{cuenta}'"""
    conexion.cursor.execute(sql)
    cuenta_encontrada=conexion.cursor.fetchone()
  
    conexion.cerrar()
    if cuenta_encontrada==None:
        
        return None
    else:
       
        cuenta_encontrada=list(cuenta_encontrada)
        cuenta_encontrada=cuenta_encontrada[0]
        return cuenta_encontrada


def guardar_datos_cuentas(Cuentas_Personas):
    conexion=ConexionDB()

    sql=f"""INSERT INTO cuentas (nombre,dni,contacto_telefono,contacto_direccion,calificacion)
    VALUES ('{Cuentas_Personas.nombre}','{Cuentas_Personas.dni}','{Cuentas_Personas.contacto_telefono}','{Cuentas_Personas.contacto_direccion}','{Cuentas_Personas.calificacion}')
    
    """
     
    conexion.cursor.execute(sql)
    conexion.cerrar()

def guardar_datos_creditos(Creditos):
    conexion=ConexionDB()

    sql=f"""INSERT INTO creditos (cuenta,cuotas,productos,monto_base,telefono_garante,direccion_garante,judiciales,estado)
    VALUES ('{Creditos.cuenta}','{Creditos.cuotas}','{Creditos.productos}','{Creditos.monto_base}','{Creditos.telefono_garante}','{Creditos.direccion_garante}','{Creditos.judiciales}','{Creditos.estado}')
    
    """
     
    conexion.cursor.execute(sql)
    conexion.cerrar()

def guardar_datos_fechas(Fechas_Vencimiento,numero):
    conexion=ConexionDB()
    dia_delta=datetime.timedelta(days=30)
    Fechas_Vencimiento.fecha= Fechas_Vencimiento.fecha+dia_delta
    fecha_vencimiento=datetime.datetime.strftime(Fechas_Vencimiento.fecha,"%Y/%m/%d")
    sql=f"""INSERT INTO fechas_pagos (fecha,monto_base,estado,al_dia,cuenta,credito)
        VALUES ('{fecha_vencimiento}','{Fechas_Vencimiento.monto_base}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.al_dia}','{Fechas_Vencimiento.cuenta}','{Fechas_Vencimiento.credito}')
    
        """
    conexion.cursor.execute(sql)
    for fecha in range (numero-1): 
        Fechas_Vencimiento.fecha= Fechas_Vencimiento.fecha+dia_delta
        fecha_vencimiento=datetime.datetime.strftime(Fechas_Vencimiento.fecha,"%Y/%m/%d")
        sql=f"""INSERT INTO fechas_pagos (fecha,monto_base,estado,al_dia,cuenta,credito)
        VALUES ('{fecha_vencimiento}','{Fechas_Vencimiento.monto_base}','{Fechas_Vencimiento.estado}','{Fechas_Vencimiento.al_dia}','{Fechas_Vencimiento.cuenta}','{Fechas_Vencimiento.credito}')
    
        """
        conexion.cursor.execute(sql)
    conexion.cerrar()
def pagos_cuotas(Pagos,fecha_id):
    conexion=ConexionDB()

    sql=f"""INSERT INTO pagos (fecha_pago,monto_pagado,fecha_id,id_cliente)
    VALUES ('{Pagos.fecha_pago}','{Pagos.monto_pagado}','{Pagos.fecha_id}','{Pagos.id_cliente}')
    
    """
    sql_2=f"""update fecha_vencimientos set estado=0 where fecha_id='{fecha_id}'
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cursor.execute(sql_2)
        conexion.cerrar()
        
    except:
        titulo=" error al registrar el pago"
        mensaje= "Verifique los campos, puede que falte alguno o que algun campo no fue llenado con su tipo valido" 
        messagebox.showerror(titulo,mensaje)
    

def busquedadni(dni):
    conexion=ConexionDB()
    lista_cliente=[]
    try:
        
        sql=f""" SELECT id_clientes,nombre, producto FROM datos_clientes WHERE dni like '%{dni}%' AND estado =1"""
        conexion.cursor.execute(sql)
        lista_cliente=conexion.cursor.fetchall()
        conexion.cerrar()
        return lista_cliente
    except:
           titulo=" error al buscar credito"
           mensaje= "el dni ingresado no esta asociado a ningún credito" 
           messagebox.showerror(titulo,mensaje)

           return lista_cliente

    
def fin_credito(id_cliente):
    conexion=ConexionDB()
    sql_2=f"""update datos_clientes set estado=0 where id_clientes='{id_cliente}'
    """
    
    
    conexion.cursor.execute(sql_2)
    conexion.cerrar()


def busquedanombre(nombre):
    lista_cliente=[]
    try:
        conexion=ConexionDB()
        
        variable="%"
        sql=f""" SELECT id_clientes,nombre, producto FROM datos_clientes WHERE nombre like '%{nombre}%' AND estado =1
    """
        conexion.cursor.execute(sql)
        lista_cliente =conexion.cursor.fetchall()
        conexion.cerrar()
        return lista_cliente
       

    except:
         titulo=" error al buscar credito"
         mensaje= "el nombre ingresado no esta asociado a ningún credito" 
         messagebox.showerror(titulo,mensaje)
         return lista_cliente


def faltante_pagar(ide):
    conexion=ConexionDB()

    sql=f"""SELECT monto_base,al_dia FROM fecha_vencimientos WHERE idcliente='{ide}' AND estado=1"""
    total=0.0
    conexion.cursor.execute(sql)
    algo=[]
    algo=conexion.cursor.fetchall()
    
    
    cuotas_restantes=len(algo)
    """if (cuotas_restantes==0):
        cuotas_restantes=cuotas"""
        
    
    
    if (lista_vacia(algo)== False ):
            
           for i in range(cuotas_restantes):
                algo_1=algo[i]
                algo_2=list(algo_1)
                al_dia=algo_2[1]
                monto=algo_2[0]
                if(al_dia):
                 total=total+monto
                else: 
                    total=total+monto*1.13
       
           conexion.cerrar()
           return total     
    else: 
        
        return 0
def lista_vacia(lista):
        return not lista


def borrar_cliente(ide):
    fin_credito(ide)
    conexion=ConexionDB()
    sql_1=f"""update fecha_vencimientos set estado=0 where idcliente='{ide}'
    """
    conexion.cursor.execute(sql_1)
    conexion.cerrar()