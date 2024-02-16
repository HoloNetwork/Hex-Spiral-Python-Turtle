import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')

colors=['yellow', 'orange', 'red', 'purple', 'blue', 'green']
max_length = 280
current_length = 0

for x in range(360):
    if current_length == max_length:
        break
    t.pencolor(colors[x%6])
    t.width(x/150)
    t.forward(x)
    t.left(55)
    current_length += 1

turtle.done()
