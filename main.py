import math
import turtle

def draw_shape(shape,p,f):
    t = turtle.Turtle()
    t.speed(2)
    t.pensize(3)
    turtle.setpos(0,0)
    t.pencolor(p)
    t.fillcolor(f)
    t.begin_fill()

    if  "square" in shape:
        for i in range(4):
            t.forward(100)
            t.right(90)

    if "triangle" in shape:
        for i in range(3):
            t.forward(100)
            t.left(120)

    if "circle" in shape:
        t.circle(50)

    if "pentagon" in shape:
        for i in range(5):
            t.forward(80)
            t.right(72)

    if "hexagon" in shape:
        for i in range(6):
            t.forward(70)
            t.right(60)

    if "heptagon" in shape:
        for i in range(7):
            t.forward(60)
            t.right(51.42)

    if "octagon" in shape:
        for i in range(8):
            t.forward(50)
            t.right(45)

    if "nonagon" in shape:
        for i in range(9):
            t.forward(45)
            t.right(40)

    if "decagon" in shape:
        for i in range(10):
            t.forward(40)
            t.right(36)

    if "right angle triangle" in shape:
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(135)
        t.forward(142)

    if "scalene triangle" in shape:
        t.forward(100)
        t.left(120)
        t.forward(70)
        t.left(100)
        t.forward(100)

    if "parallelogram" in shape:
        t.forward(100)
        t.left(60)
        t.forward(50)
        t.left(120)
        t.forward(100)
        t.left(60)
        t.forward(50)

    if "trapezium" in shape:
        t.forward(50)  
        t.right(45)  
        t.forward(100)  
        t.right(135)  
        t.forward(200)  
        t.right(135)  
        t.forward(100)
    

    if "four pointed star" in shape:
         n = 4
         angle = 180 - 180 / n
         for i in range(2*n):
            t.forward(200)
            t.right(angle)

    elif "six pointed star" in shape:
            t.penup()
            t.goto(0, 0)
            t.pendown()
            for k in range(6):
                t.forward(100)
                t.right(60)
                t.forward(100)
                t.left(120)

    elif "star" in shape:
        for i in range(5):
            t.forward(150)
            t.right(144)

    
    t.end_fill()    
    t.hideturtle()
    try:
       turtle.done()
    except:
        pass



def pattern(shape):
    size=5

    if "square pattern" in shape:
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    elif "triangle pattern" in shape:
        for i in range(1, size+1):
            for j in range(1, size-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if i == size or j == 1 or j == 2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    elif "circle pattern" in shape:
            for i in range((2 * size)+1):
               for j in range((2 * size)+1):
                  dist = math.sqrt((i - size) * (i - size) + (j - size) * (j - size))
                  if (dist > size - 0.5 and dist < size + 0.5): 
                        print("*",end="")
                  else:
                        print(" ",end="")      
               print()

    elif "rectangle pattern" in shape:
        for i in range(size):
            for j in range(size + 5):
                if i == 0 or i == size - 1 or j == 0 or j == size + 5 - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    elif "diamond pattern" in shape:
        for i in range(1, size+1):
            for j in range(1,size-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

        for i in range(size-1,0, -1):
            for j in range(1,size-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    else:
            print("Sorry, I don't know how to draw that pattern.")     

def chatbot():
    shapes=["square","triangle","circle","pentagon","hexagon","octagon","nonagon","decagon","right angle triangle","scalene triangle",
            "parallelogram","trapezium","star"]

    total=["square","triangle","circle","pentagon","hexagon","octagon","nonagon","decagon","right angle triangle","scalene triangle",
           "parallelogram","trapezium","star","four pointed star","six pointed star","square pattern","triangle pattern",
           "circle pattern","rectangle pattern","diamond pattern"]
    
    p="black"
    f="white"

    print("Hi, I'm a Chatbot that can draw shapes!")
    print("To draw a shape, simply type the name of the shape you want to draw.")
    
    while True:
        flag=0
        user_input = input("Enter your query or the shape which you want to be drawn:")

        if "exit" in user_input.lower() or "bye" in user_input.lower():
            print("Goodbye!")
            break

        elif ("help" in user_input):
            print("I can draw the following shapes:")
            print(total)

        elif("pattern" in user_input.lower()):
            pattern(user_input.lower())

        elif("color" in user_input.lower() or "colour" in user_input.lower()):
            p=input("Enter the outline colour: ")
            f=input("Enter the fill colour: ")

        else:
            for s in shapes:
                if s in user_input.lower():
                    draw_shape(user_input.lower(),p,f)
                    flag=1
                    try:
                        turtle.done()
                    except:
                        pass
                    break
            if (flag!=1):
                print("Sorry, I don't know how to draw that shape.")
chatbot()
