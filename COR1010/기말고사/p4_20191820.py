import turtle as t

def drawTri(C,L):
    t.fillcolor(C)
    t.begin_fill()
    for i in range(3):
        t.fd(L)
        t.lt(360/3)
    t.end_fill()

def drawSquare(C,L):
    t.fillcolor(C)
    t.begin_fill()
    for i in range(4):
        t.fd(L)
        t.lt(360/4)
    t.end_fill()


t.shape('turtle')
t.pencolor('red')
drawSquare('green',120)
t.up()
t.goto(-20,120)
t.down()
drawTri('yellow',160)

