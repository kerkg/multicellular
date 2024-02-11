import turtle
import config
import tkinter as tk
from tkinter import colorchooser


def square_function(start_pos: tuple[float, float], width: float = 1, height: float = 1, color: str = config.config["cell"]["default_color"]) -> None:
    # draws a colored square. Example: square_function((10, 10), 10, 10, "#3c3c78")
    # arg1= start_pos: starting position, arg2= width: width of your square, arg3= height.height of your square,
    # arg4=color: color of your square

    # initializing square_function
    if turtle.xcor() != start_pos[0]:
        turtle.penup()
        turtle.setx(start_pos[0])
        turtle.pendown()
    if turtle.ycor() != start_pos[1]:
        turtle.penup()
        turtle.sety(start_pos[1])
        turtle.pendown()
    # drawing a cel
    turtle.color(color)
    turtle.begin_fill()
    turtle.setx(turtle.xcor()+width)
    turtle.sety(turtle.ycor()-height)
    turtle.setx(turtle.xcor()-width)
    turtle.sety(turtle.ycor()+height)
    turtle.done()
    turtle.end_fill()


def cell_color_chooser() -> str:
    # color chooser( made by chat gpt)
    # opens the color chooser dialog
    root = tk.Tk()
    root.withdraw()
    color: tuple[tuple[int, int, int], str] = colorchooser.askcolor(title="colorchooser")
    return color[1]

