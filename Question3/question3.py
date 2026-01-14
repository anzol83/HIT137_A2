import turtle
import math

def inward_koch_edge(t, length, depth):
    # Base case: just draw the line
    if depth == 0:
        t.forward(length)
        return

    # Break the line into 3 parts
    third = length / 3

    # Recursion + inward triangle indentation
    inward_koch_edge(t, third, depth - 1)
    t.left(60)
    inward_koch_edge(t, third, depth - 1)
    t.right(120)
    inward_koch_edge(t, third, depth - 1)
    t.left(60)
    inward_koch_edge(t, third, depth - 1)

def draw_polygon(sides, side_length, depth):
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Rough centering using polygon radius idea
    radius = side_length / (2 * math.sin(math.pi / sides))
    t.penup()
    t.goto(-side_length / 2, -radius / 2)
    t.pendown()

    for _ in range(sides):
        inward_koch_edge(t, side_length, depth)
        t.left(360 / sides)

    turtle.done()

def main():
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))
    depth = int(input("Enter recursion depth: "))

    draw_polygon(sides, side_length, depth)

if __name__ == "__main__":
    main()