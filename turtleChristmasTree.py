import turtle
import random

def draw_star(t, size):
    t.penup()
    t.left(90)
    t.forward(size * 3)
    t.right(90)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_ornament(t, size):
    colors = ["red", "blue", "yellow", "purple", "orange"]
    t.penup()
    t.color(random.choice(colors))
    t.begin_fill()
    t.circle(size/10)
    t.end_fill()

def draw_tree():
    screen = turtle.Screen()
    screen.bgcolor("skyblue")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    
    # Draw trunk
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    # Draw tree layers
    y = -100
    size = 200
    layers = 3
    
    for _ in range(layers):
        t.penup()
        t.goto(-size/2, y)
        t.pendown()
        t.color("green")
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
        
        # Add ornaments
        for _ in range(5):
            t.penup()
            t.goto(random.randint(int(-size/2+20), int(size/2-20)), 
                  random.randint(int(y), int(y+size/2)))
            draw_ornament(t, size)
        
        y += size/2
        size -= 50
    
    # Add star on top
    draw_star(t, 30)
    
    # Add snow
    t.penup()
    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-200, 300)
        t.goto(x, y)
        t.color("white")
        t.dot(5)
    
    screen.exitonclick()

# Run the program
draw_tree()