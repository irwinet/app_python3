import turtle as t #cargamos el modulo de la tortuga

t.setup(500,500) #configuramos un espacio de dibujo

#TODO programar aqui
t.shape("turtle")
t.color("green")

#backward
#right
#penup
#pendown

#400 ancho 300 alto

print(t.pos())
t.penup()
t.forward(200)
t.left(90)
t.pendown()
t.forward(150)
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(150)
print(t.pos())

t.done() #igualmente debemos poner abajo del todo
t.bye() #cerrar las rutinas