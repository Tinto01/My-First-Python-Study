import turtle

# Create a turtle
t = turtle.Turtle()

# Set the fill color to light blue
t.color("lightblue")

# Start filling
t.begin_fill()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward 100 pixels
    t.right(90)     # Turn right 90 degrees

# End filling
t.end_fill()

# Keep the window open
turtle.done()