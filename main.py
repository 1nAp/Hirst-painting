# THE COMMENTED OUT CODE IS ONLY USED ONCE TO GET THE LIST OF COLORS FROM A GIVEN PICTURE.
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

#Importing necessary modules
import turtle as t
import random

#List of colors gotten from the commented out code.
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


#Basic setup of the turtle object (position, setting color mode to RGB, creating object from class)
turtle = t.Turtle()
t.colormode(cmode=255)
turtle_x = -300
turtle.ht()
turtle.penup()
turtle.goto(turtle_x, -200)

#The first for-loop runs the second for-loop 10 times followed by lifting the pen and moving up a row)
for _ in range(10):
    #The second for-loop draws 10 dots in a row with random colors from the color_list.
    for _ in range(10):
        turtle.pendown()
        turtle.dot(20, random.choice(color_list))
        turtle.penup()
        turtle.fd(50)
    turtle.penup()
    turtle.goto(turtle_x, turtle.ycor()+50)


#Changes the behavior of the GUI to only disappear after clicking within the window.
screen = t.Screen()
screen.exitonclick()


