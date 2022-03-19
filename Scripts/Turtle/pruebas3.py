import turtle as t #cargamos el modulo de la tortuga

t.setup(500,500) #configuramos un espacio de dibujo

#TODO programar aqui
t.shape("turtle")
t.color("green")

def rectangulo(px,py,ancho,alto):
    t.penup()
    t.goto(px+ancho/2, py+alto/2)
    #t.left(180)
    t.seth(180)
    t.pendown()
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)

rectangulo(0,0,400,300)
rectangulo(0,0,300,200)
rectangulo(0,0,200,100)
rectangulo(0,0,50,50)

t.done() #igualmente debemos poner abajo del todo
t.bye() #cerrar las rutinas