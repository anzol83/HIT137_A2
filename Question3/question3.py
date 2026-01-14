import turtle
import math

def inward_koch_edge(t: turtle.Turtle, length: float, depth: int) -> None:
    """
    Takes one straight edge and turns it into a 'dent' pattern.
    If depth is 0, it just draws the straight line.
    """
    # Stop recursion and draw normal line
    if depth == 0:
        t.forward(length)
        return

    # Split the edge into three equal parts
    third = length / 3.0

    # Draw 4 smaller edges with triangle indentation in the middle
    inward_koch_edge(t, third, depth - 1)
    t.left(60)
    inward_koch_edge(t, third, depth - 1)
    t.right(120)
    inward_koch_edge(t, third, depth - 1)
    t.left(60)
    inward_koch_edge(t, third, depth - 1)

def draw_recursive_polygon(sides: int, side_length: float, depth: int) -> None:
    # Setup screen
    screen = turtle.Screen()
    screen.title("HIT137 - Q3 Recursive Turtle Pattern")
    screen.tracer(0, 0)

    # Setup turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Move the turtle so the drawing looks centered
    radius = side_length / (2.0 * math.sin(math.pi / sides))
    t.penup()
    t.goto(-side_length / 2.0, -radius / 2.0)
    t.setheading(0)
    t.pendown()

    # Draw each side using recursion
    for _ in range(sides):
        inward_koch_edge(t, side_length, depth)
        t.left(360.0 / sides)

    screen.update()
    turtle.done()

def main() -> None:
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Simple validation
    if sides < 3:
        raise ValueError("Number of sides must be at least 3.")
    if side_length <= 0:
        raise ValueError("Side length must be positive.")
    if depth < 0:
        raise ValueError("Recursion depth must be 0 or more.")

    draw_recursive_polygon(sides, side_length, depth)

if __name__ == "__main__":
    main()