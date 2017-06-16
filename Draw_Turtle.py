import turtle
def dr_shape(square):
    for i in range(1,4):

        square.right(90)
        square.forward(100)
        sqaure.backward(50)
        square.right(120)
   

def dr_art():
    #wind = turtle.Screen()
    #wind.bgcolor("blue")
    #sam = turtle.Turtle()
    #sam.shape("turtle")
    #sam.color("yellow")
    #sam.speed(2)
    #for j in range(1,19):
            #dr_shape(sam)
    #sam.right(20)
    turtle.write("messi fan", font=("Arial", 16, "normal"))
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("red")               
    brad.circle(100)
    
    
    #wind.exitonclick()

    
    
dr_art()
