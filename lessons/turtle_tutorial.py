from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -50)
leo.pendown()

leo.color("blue")
colormode(255)
leo.color(150, 191, 46)

leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0 
while i < 3: 
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()

bob.penup()
bob.goto(-150, -50)
bob.pendown()

bob.color("black")
colormode(255)
bob.color(4, 4, 4)

bob.speed(70)
bob.hideturtle()

i: int = 0 
while i < 3: 
    bob.forward(300)
    bob.left(120)
    i += 1

side_length: int = 300

bob.penup()
bob.goto(-150, -50)
bob.pendown()

bob.color("black")
colormode(255)
bob.color(4, 4, 4)

bob.speed(70)
bob.hideturtle()

i: int = 0 
while i < 101: 
    bob.forward(side_length * 0.97)
    bob.left(123)
    i += 1
done()