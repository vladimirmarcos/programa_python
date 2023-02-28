from conexion_db import DataBase
from tkinter import messagebox





def listar():
    conexion=ConexionDB()
    lista_creditos=[]
    sql='SELECT * FROM creditos'

    conexion.cursor.execute(sql)
    lista_creditos=conexion.cursor.fetchall()
    conexion.cerrar()
    return lista_creditos