import turtle
import config
import tkinter as tk
import struct
# import gc
import functools
from tkinter import colorchooser


@functools.cache
def rgb_to_hex(r: int, g: int, b: int) -> str:
    # returns the hex value of the rgb value NOTE:parameters must be between 0 and 255(including 0 and 255) otherwise
    # turtle will throw an error(probably bad color sequence error)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


@functools.cache
def hex_to_rgb(hxcode: str):
    # returns the rgb value of the given hex code
    return struct.unpack('BBB', bytes.fromhex(hxcode.strip("#")))


def square_function(start_pos: tuple[float, float] = (turtle.xcor(), turtle.ycor()), width: float = 1,
                    height: float = 1, color=config.config["cell"]["default_color"]) -> str:
    # draws a colored square. Example: square_function((10, 10), 10, 10, "#3c3c78")
    # arg1= start_pos: starting position, arg2= width: width of your square, arg3= height:height of your square,
    # arg4=color: color of your square for example: >color= "#000000"< or >color= (0,0,0)<

    # initializing square_function

    if type(color) is tuple:
        color_t = rgb_to_hex(color[0], color[1], color[2])
        color = color_t
        del color_t
    if turtle.xcor() != start_pos[0]:
        turtle.penup()
        turtle.setx(start_pos[0])
        turtle.pendown()
    if turtle.ycor() != start_pos[1]:
        turtle.penup()
        turtle.sety(start_pos[1])
        turtle.pendown()
    # drawing a cel
    turtle.tracer()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setx(turtle.xcor()+width)
    turtle.sety(turtle.ycor()-height)
    turtle.setx(turtle.xcor()-width)
    turtle.sety(turtle.ycor()+height)
    turtle.end_fill()
    return f"({start_pos})({width},{height})({color})"


def page_gen_function(pargf_obj) -> None:  # this is the func that specializes in drawing the whole screen
    # processes the screen matrices
    turtle.tracer()
    # drawing a cel
    for cell_obj in pargf_obj:
        turtle.color(rgb_to_hex(cell_obj[1][0], cell_obj[1][1], cell_obj[1][2]))
        turtle.begin_fill()
        turtle.setx(turtle.xcor()+cell_obj[0][0])  # +width
        turtle.sety(turtle.ycor()-cell_obj[0][1])  # -height
        turtle.setx(turtle.xcor()-cell_obj[0][0])  # -width
        turtle.sety(turtle.ycor()+cell_obj[0][1])  # +height
        turtle.end_fill()


def cell_color_chooser() -> str:
    # color chooser( made by chatgpt)
    # opens the color chooser dialog
    root = tk.Tk()
    root.withdraw()
    color: tuple[tuple[int, int, int], str] = colorchooser.askcolor(title="colorchooser")
    return color[1]


# def init() -> None:
#     turtle.setup(width=1.0, height=1.0)
#     turtle.hideturtle()



