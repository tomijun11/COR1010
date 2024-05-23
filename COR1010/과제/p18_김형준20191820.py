# 20191820 김형준
import turtle as t

t.shape("turtle")

t.color("RED","GREEN")
t.begin_fill()
for i in range(3):
    t.fd(100)
    t.rt(90)
t.fd(100)
t.end_fill()

t.rt(30)
t.fillcolor("YELLOW")
t.begin_fill()
for i in range(1):
    t.fd(100)
    t.lt(240)
t.fd(100)
t.end_fill()
