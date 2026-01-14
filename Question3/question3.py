import turtle
import math

def inward_koch_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    third = length / 3
    inward_koch_edge(t, third, depth - 1)
    t.left(60)
    inward_koch_edge(t, third, depth - 1)
    t.right(120)
    inward_koch_edge(t, third, depth - 1)
    t.left(60)
    inward_koch_edge(t, third, depth - 1)

def draw_recursive_polygon(sides, side_length, depth):
    screen = turtle.Screen()
    screen.title("HIT137 - Q3 Recursive Turtle Pattern")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    radius = side_length / (2 * math.sin(math.pi / sides))
    t.penup()
    t.goto(-side_length / 2, -radius / 2)
    t.pendown()

    for _ in range(sides):
        inward_koch_edge(t, side_length, depth)
        t.left(360 / sides)

    screen.update()
    turtle.done()

def main():
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    if sides < 3:
        raise ValueError("Number of sides must be at least 3.")
    if side_length <= 0:
        raise ValueError("Side length must be positive.")
    if depth < 0:
        raise ValueError("Recursion depth must be 0 or more.")

    draw_recursive_polygon(sides, side_length, depth)

if __name__ == "__main__":
    main()