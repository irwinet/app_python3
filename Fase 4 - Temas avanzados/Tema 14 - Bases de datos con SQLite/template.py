import sqlite3

conexion = sqlite3.connect("namedb.db")
cursor = conexion.cursor()





conexion.commit()
conexion.close()