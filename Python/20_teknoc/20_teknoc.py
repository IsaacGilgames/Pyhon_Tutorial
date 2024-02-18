#teknoc.py

import turtle

hossz = 100
turtle.color('red')
turtle.pensize(5)
turtle.speed(3)

for j in range(36):
    for i in range(4):
        turtle.forward(hossz)
        turtle.right(90)
    turtle.right(10)
    hossz+= 10



turtle.exitonclick()