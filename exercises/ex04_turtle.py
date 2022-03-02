"""TODO: Describe your scene program."""

__author__ = "730523395"


from turtle import Turtle, colormode, done
from random import randint


def main() -> None: 
    """The entrypoint of my scene."""
    final_pic: Turtle = Turtle()
    final_pic.speed(25) 
    final_pic.hideturtle()
    sun(final_pic, -300, 300, 10)
    x = 120
    y = 5
    width = 25
    i: int = 0 
    while i < 8:
        mountain_land(final_pic, x, y, width)
        x += -50 
        width += 50
        i += 1
    water(final_pic, -290, 0, 10)
    boat_one(final_pic, -45, -150, 10)
    boat_two(final_pic, -20, -125, 10)
    boat_three(final_pic, -50, -136, 10)
    boat_cover(final_pic, -47, -103, 10)
    x = 100
    y = 250 
    i = 0
    while i < 2:
        starry_sky(final_pic, x, y)
        x += -50 
        y += 15
        i += 1
    done()


def starry_sky(star: Turtle, x: float, y: float) -> None: 
    """Making the north star and big dipper with a pink pen."""
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color("pink")
    colormode(255)
    star.color(244, 144, 216)
    side_length: int = 40
    i = 0
    while i < 15: 
        star.forward(side_length * 0.97)
        star.left(550)
        i += 1
        

def mountain_land(a_mountain: Turtle, x: float, y: float, width: float) -> None: 
    """Drawing a green mountain landscape that overlaps and sits on top of the lake."""
    a_mountain.penup()
    a_mountain.goto(x, y) 
    a_mountain.pendown()
    a_mountain.color("green", "dark green")
    colormode(255)
    a_mountain.color(38, 168, 12)
    a_mountain.fillcolor(9, 86, 28)
    a_mountain.begin_fill()
    i = 0 
    while i < 3: 
        a_mountain.forward(150)
        a_mountain.left(120)
        i += 1
    a_mountain.end_fill()


def sun(sun: Turtle, x: float, y: float, width: float) -> None:
    """Randomizing the placement of the sun."""
    sun.penup()
    sun.goto(randint(-300, 0), randint(0, 300))
    sun.pendown()
    sun.color("orange")
    colormode(255)
    sun.color(255, 198, 26)
    sun.begin_fill() 
    sun.circle(60)
    sun.end_fill()


def water(lake: Turtle, x: float, y: float, width: float) -> None:
    """Drawing a large body of water that is supposed to be a lake under the mountain landscape."""
    lake.penup()
    lake.goto(x, y)
    lake.pendown()
    lake.color("blue")
    colormode(255)
    lake.color(12, 117, 168)
    lake.begin_fill()
    i: int = 0 
    while i < 4: 
        lake.forward(600)
        lake.right(90)
        i += 1
    lake.end_fill()


def boat_cover(square: Turtle, x: float, y: float, width: float) -> None:
    """Covering up the top curve of the boat to make it look more like a boat from viewer's pint of view instead of bird's eye."""
    square.penup()
    square.goto(x, y)
    square.pendown()
    square.color("blue")
    colormode(255)
    square.color(12, 117, 168)
    square.begin_fill()
    square.begin_fill()
    i: int = 0 
    while i < 4: 
        square.forward(30)
        square.left(90)
        i += 1
    square.end_fill()


def boat_one(left_piece: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the left triangle of the boat."""
    left_piece.penup()
    left_piece.goto(x, y)
    left_piece.pendown()
    left_piece.setheading(90.0)
    left_piece.color("brown")
    colormode(255)
    left_piece.color(81, 62, 56)
    left_piece.begin_fill()
    i = 0
    while i < 3:
        left_piece.forward(25)
        left_piece.left(120)
        i += 1
    left_piece.end_fill()


def boat_two(right_piece: Turtle, x: float, y: float, width: float) -> None:
    """Drawing the right triangle of the boat."""
    right_piece.penup()
    right_piece.goto(x, y)
    right_piece.pendown()
    right_piece.setheading(-90.0)
    right_piece.begin_fill()
    i = 0
    while i < 3:
        right_piece.forward(25)
        right_piece.left(120)
        i += 1
    right_piece.end_fill()


def boat_three(middle_piece: Turtle, x: float, y: float, width: float) -> None:
    """Drawing middle piece of an attempted boat."""
    middle_piece.penup()
    middle_piece.goto(x, y)
    middle_piece.pendown()
    middle_piece.begin_fill()
    middle_piece.circle(18)
    middle_piece.end_fill()


if __name__ == "__main__":
    main()
