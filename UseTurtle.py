import turtle
def art():
    turtle.speed()
    window=turtle.Screen()
    window.bgcolor("black")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    for i in range(1,37):
        i=4;
        while i>0:
            brad.forward(100)
            brad.right(90)
            i=i-1
        brad.right(10)
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("white")
    angie.right(90)
    angie.forward(250)
    window.exitonclick()
art()
        
