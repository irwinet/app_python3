import turtle as t #cargamos el modulo de la tortuga

t.setup(500,500) #configuramos un espacio de dibujo

#TODO programar aqui
t.shape("turtle")
t.color("green")

print(t.pos())
t.forward(250)
t.left(90)
t.forward(250)
t.left(90)
t.forward(500)
t.left(90)
t.forward(500)
t.left(90)
t.forward(500)
print(t.pos())

t.done() #igualmente debemos poner abajo del todo
t.bye() #cerrar las rutinas