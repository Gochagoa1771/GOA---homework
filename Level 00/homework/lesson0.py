from turtle import *

#we want to paint a house

#step 1: draw a squeare
speed(30)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#endof squere

#drawing a door

forward(70)
color("pink")
left(90)
forward(120) # height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(60, 110)
pendown()
right(60)
width(4)
forward(50)
right(90)
forward(65)
right(90)
forward(50)
right(90)
forward(65)
penup()
goto(140, 110)
pendown()
right(180)
forward(65)
right(90)
forward(50)
right(90)
forward(65)
right(90)
forward(50)
exitonclick()
