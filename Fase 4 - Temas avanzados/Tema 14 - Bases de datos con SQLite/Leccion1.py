import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE usuarios(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

#cursor.execute("INSERT INTO usuarios VALUES ('Irwin',27,'irwin@gmail.com')")

#cursor.execute("SELECT * FROM usuarios")
#print(cursor)
# usuario = cursor.fetchone()
# print(usuario[0])

# usuarios = [
#     ("Juan",23,"juan@gmail.com"),
#     ("Jose",16,"jose@gmail.com"),
#     ("Pedro",12,"pedro@gmail.com"),
# ]
# cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)", usuarios)

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
#print(usuarios)

for usuario in usuarios:
    print("Nombre: ",usuario[0]," - Email:", usuario[2])

conexion.commit()

conexion.close()