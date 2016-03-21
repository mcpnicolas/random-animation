#draw random colored dots

import turtle
import random
import math

def generate_dot_coord(dots):
    xy_coord = []
    for i in range(2):
        xy_coord.append(random.randint(-250,250))
    xy_coord = tuple(xy_coord)
    return xy_coord

def hex_code_color(rgb):
    hex_color = "#"
    for color in rgb:
        hex_color_0x = hex(color)
        if len(hex(color)) == 3:
            hex_color += "0" + hex_color_0x[2:].upper()
        else:
            hex_color += hex_color_0x[2:].upper()
    print(hex_color)

def generate_dot_color(dots):
    rgb1 = []
    rgb2 = []
    for value in range(3):
        rgb1.append(random.randint(0,255))
        rgb2.append(random.randint(0,255))
    color_diffs = []
    for color in range(3):
        color_diffs.append(math.fabs(rgb1[color]-rgb2[color]))
    r = rgb1[0]
    g = rgb1[1]
    b = rgb1[2]
    current_rgb = [r, g, b]
    colors_of_dots = []
    for i in range(dots+2):
        for value in range(3):
            if rgb1[value] > rgb2[value]:
                current_rgb[value] = (current_rgb[value]-int(color_diffs[value]/(dots+2)))
            elif rgb1[value] < rgb2[value]:
                current_rgb[value] = (current_rgb[value]+int(color_diffs[value]/(dots+2)))
        current_r = current_rgb[0]
        current_g = current_rgb[1]
        current_b = current_rgb[2]
        colors_of_dots.append([current_r, current_g, current_b])
    rgb2 = colors_of_dots[len(colors_of_dots)-1]
    print("start color",rgb1)
    print("end color",rgb2)
    hex_code_color(rgb1)
    hex_code_color(rgb2)
    return colors_of_dots

def turtle_setup():
    turtle.speed(3)
    turtle.setup(750,750)
    turtle.title("Randomized Art")
    turtle.colormode(255)
    turtle.color(255,255,255)

def draw_random_dots(dots):
    first_coord = generate_dot_coord(dots)
    turtle.goto(first_coord)
    colors_of_dots = generate_dot_color(dots)
    for i in range(dots):
        xy_coord = generate_dot_coord(dots)
        turtle.color(colors_of_dots[i])
        turtle.dot(10)
        turtle.goto(xy_coord)
    turtle.color(colors_of_dots[len(colors_of_dots)-2])
    turtle.dot(10)
    turtle.goto(first_coord)
    turtle.color(colors_of_dots[len(colors_of_dots)-1])
    turtle.dot(10)

def main(loop_on, dots):
    #dots = int(input("How many dots? "))
    while loop_on:
        turtle_setup()
        draw_random_dots(dots)
        turtle.clear()
        print("")
    if not loop_on:
        turtle_setup()
        draw_random_dots(dots)

#endless loop - True
#run once - False
#num of dots-1
main(True, 14)
