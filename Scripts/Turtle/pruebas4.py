import turtle as t #cargamos el modulo de la tortuga

t.setup(500,500) #configuramos un espacio de dibujo

#TODO programar aqui
t.shape("turtle")
t.color("green")

def poligono_regular(px,py,radio,lados):
    t.penup()
    t.goto(px,py-radio)
    #t.pendown()
    t.circle(radio)

    angulo = 360/lados
    print(angulo)

    vertices = []

    for i in range(lados):
        t.penup()
        t.goto(px,py)
        #t.pendown()

        t.seth(angulo*i+1)
        t.forward(radio)
        #print(t.pos())
        vertices.append(t.pos())

    t.penup()
    t.goto(vertices[-1])
    t.pendown()

    for v in vertices:
        t.goto(v)

#poligono_regular(0,0,100,7)
t.speed(200)
for n in range(3,21):
    poligono_regular(0,0,n*10,n)


t.done() #igualmente debemos poner abajo del todo
t.bye() #cerrar las rutinas