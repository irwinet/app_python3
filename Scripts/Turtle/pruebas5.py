import turtle as t #cargamos el modulo de la tortuga

t.setup(500,500) #configuramos un espacio de dibujo

#TODO programar aqui
t.shape("turtle")
t.color("green")

# def ordenar():
#     order = t.textinput("Orden requerida",
#     "Movimientos: a w s d - Salir: e"
#     )

#     if order == "d": t.seth(0)
#     elif order == "w": t.seth(90)
#     elif order == "a": t.seth(180)
#     elif order == "s": t.seth(270)
#     elif order == "e": t.bye()
#     else: return

#     t.forward(50)

# while True:
#     ordenar()

def derecha():
    t.seth(0)
    t.forward(20)

def izquierda():
    t.seth(180)
    t.forward(20)

def arriba():
    t.seth(90)
    t.forward(20)

def abajo():
    t.seth(270)
    t.forward(20)

def salir():
    t.bye()

t.onkey(arriba, "w")
t.onkey(izquierda, "a")
t.onkey(derecha, "d")
t.onkey(abajo, "s")
t.onkey(salir, "e")

t.listen()

t.done() #igualmente debemos poner abajo del todo
t.bye() #cerrar las rutinas