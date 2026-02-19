# from turtle import Turtle, Screen
import random
import turtle as t
#if use import turtle, then need to type turtle.Turtle() all the time
# import turtle
#tim=turtle.Turtle()
#create a list of colours
colours=["red","green","blue","yellow","purple","orange","pink","brown","gray","black"]
#from turtle import * will import all the functions from turtle module
#import turtle as t will import the turtle module and give it an alias t

direction=[0,90,180,270]
timmy_the_turtle=t.Turtle()
# timmy_the_turtle.pensize(15)




def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

#Chanllenge1-draw a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

#challenge2-draw a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#challenge3-draw differenrt shapoes
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)


#challenge4-draw a random walk wigth random colors

# for _ in range(200):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))


#     timmy_the_turtle.color(random_color)


#tuple is a list of values that cannot be changed
#list is a list of values that can be changed
#tuple is defined using parentheses
#list is defined using square brackets
#tuple is defined using parentheses
# my_tuple=(1,2,3,4,5)
# my_tuple[0]


#challenge5-draw a spirograph
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy_the_turtle.color(random_color)
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)
# draw_spirograph(5)

timmy_the_turtle.speed("fastest")
t.colormode(255)
timmy_the_turtle.color(random_color())
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)
draw_spirograph(5)
screen=t.Screen()
screen.exitonclick()