import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()


# cursor.execute('''
#             CREATE TABLE usuarios(
#                 dni VARCHAR(9) PRIMARY KEY,
#                 nombre VARCHAR(100),
#                 edad INTEGER,
#                 email VARCHAR(100)
#             )
#             ''')

# usuarios = [
#     ("11111111A","Irwin",23,"irwin@gmail.com"),
#     ("22222222B","Juan",23,"juan@gmail.com"),
#     ("33333333C","Jose",16,"jose@gmail.com"),
#     ("44444444D","Pedro",12,"pedro@gmail.com"),
# ]
# cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?)", usuarios)

#cursor.execute("INSERT INTO usuarios VALUES('44444444E','Pedro',12,'pedro@gmail.com')")

# cursor.execute('''
#     CREATE TABLE productos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
# ''')

# productos = [
#     ("Teclado","Logitech",20),
#     ("Mouse","Logitech",10),
#     ("Pantalla","LG",200)
# ]

# cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos)

# cursor.execute("SELECT * FROM productos")
# productos = cursor.fetchall()

# for producto in productos:
#     print(producto)

# cursor.execute('''
#     CREATE TABLE usuarios(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ("11111111A","Irwin",23,"irwin@gmail.com"),
#     ("22222222B","Juan",23,"juan@gmail.com"),
#     ("33333333C","Jose",16,"jose@gmail.com"),
#     ("44444444D","Pedro",12,"pedro@gmail.com"),
# ]

# cursor.executemany("INSERT INTO usuarios VALUES(null, ?,?,?,?)", usuarios)

cursor.execute("INSERT INTO usuarios VALUES (null, '44444444D','Pedro',12,'pedro@gmail.com')")

conexion.commit()
conexion.close()