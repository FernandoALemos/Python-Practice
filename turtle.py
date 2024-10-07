import turtle
import colorsys

# inicial configuration
tortuga = turtle.Turtle()
tortuga.speed(0)
turtle.Screen().bgcolor("black")

# variables to color
n = 70 # cant colores
hue = 0 # color inicial

# Patrón
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 0.8)
    hue += 1/n
    tortuga.color(color)
    tortuga.left(1)
    tortuga.forward(1)

    for j in range(2):
        tortuga.left(2)
        tortuga.circle(100)

turtle.done()