from models.conexion_db import ConexionDB

def crear_tabla():
    conexion=ConexionDB()

    sql='''
    CREATE TABLE datos_personas(
        id_cliente INTEGER,
        nombre VARCHAR(100) NOT NULL,
        dni VARCHAR(100) NOT NULL,
        garante VARCHAR(255) NOT NULL,
        contacto VARCHAR (255) NOT NULL,
        producto TEXT(255)NOT NULL,
        monto REAL NOT NULL,
        cuotas INTEGER NOT NULL,
        estado INTEGER NOT NULL,
        
        PRIMARY KEY(id_cliente AUTOINCREMENT)
    )
    '''
    sql_1='''
    CREATE TABLE creditos(
        id_cuota INTEGER,
        fecha VARCHAR(100),
        monto VARCHAR(100),
       
        PRIMARY KEY(id_cuota AUTOINCREMENT)
    )
    '''



    try:
        conexion.cursor.execute(sql)
        conexion.cursor.execute(sql_1)
        conexion.cerrar()
    except:
        pass



conexion=ConexionDB()

crear_tabla()

       