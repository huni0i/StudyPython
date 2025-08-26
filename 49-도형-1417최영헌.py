from turtle import *

shape("turtle")
up()
goto(-200, 200)
down()
color("orange")
begin_fill()

for i in range(4):
    fd(100)
    lt(90)
end_fill()

up()
goto(100, 100)
down()
begin_fill()

for i in range(3):
    fd(100)
    lt(120)
end_fill()
exitonclick()
