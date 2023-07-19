# from turtle import Turtle, Screen
import turtle as t
import random
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("cyan3")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# for _ in range(4):
#     timmy.forward(50)
#     timmy.right(90)
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# square in square
# for _ in range(3):
#     timmy.forward(50)
#     timmy.right(120)
#     timmy.forward(50)
#     #sqaure
#     for _ in range(4):
#         timmy.forward(60)
#         timmy.right(90)
#         timmy.forward(60)

# square with colors
# colors = ["crimson","red","blue"]
#
# def number_side(num_side):
#     angle = 360/num_side
#     for _ in range(num_side):
#         timmy.forward(40)
#         timmy.right(angle)
#
# for shape in range(3,11):
#     timmy.color(random.choice(colors))
#     number_side(shape)
#
# random walk
# color = ["dark violet", "red", "blue",]
# direction  = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fastest")
# for _ in range(200):
#     timmy.forward(50)
#     timmy.right(random.choice(direction))
#     timmy.color(random_color())

# spirograph
timmy.speed("fastest")


def draw_spirograph(size_of_gaps):

    for _ in range(int(360/ size_of_gaps)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gaps)
draw_spirograph(5)







screen = t.Screen()
screen.exitonclick()