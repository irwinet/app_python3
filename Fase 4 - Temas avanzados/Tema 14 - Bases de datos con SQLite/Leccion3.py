import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute("SELECT * FROM usuarios WHERE edad=23")
# usuarios = cursor.fetchall()
# print(usuarios)

#cursor.execute("UPDATE usuarios SET nombre='Apiet Travel', edad=49 WHERE dni='11111111A'")

cursor.execute("DELETE FROM usuarios WHERE id=4")

conexion.commit()
conexion.close()