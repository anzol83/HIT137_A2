import turtle
import math

def inward_koch_edge(t: turtle.Turtle, length: float, depth: int) -> None:
    """
    This function breaks one straight line into smaller pieces
    and adds an inward triangle shape in the middle.
    It keeps calling itself until depth becomes 0.
    """

    # If depth is 0, draw a straight line and stop
    if depth == 0:
        t.forward(length)
        return

    # Splitting the current line into three equal parts
    third = length / 3.0

    # First small segment
    inward_koch_edge(t, third, depth - 1)

    # Turn left to start forming the inward triangle
    t.left(60)

    # Second small segment (upward side of the triangle)
    inward_koch_edge(t, third, depth - 1)

    # Turn right more to come back down
    t.right(120)

    # Third small segment (downward side of the triangle)
    inward_koch_edge(t, third, depth - 1)

    # Turning left again so direction becomes normal
    t.left(60)

    # Final small segment
    inward_koch_edge(t, third, depth - 1)


def draw_recursive_polygon(sides: int, side_length: float, depth: int) -> None:
    # Creating the drawing window
    screen = turtle.Screen()
    screen.title("HIT137 - Q3 Recursive Turtle Pattern")

    # Creating turtle and set basic settings
    t = turtle.Turtle()
    t.hideturtle()     # Hide arrow, we only want the drawing
    t.speed(0)         # Fastest speed
    screen.tracer(0, 0)  # Turning off animation to avoid slow drawing

    # This calculation helps place the polygon near the center
    # It finds the radius of a regular polygon
    radius = side_length / (2.0 * math.sin(math.pi / sides))

    # Moving turtle to a good starting point
    t.penup()
    t.goto(-side_length / 2.0, -radius / 2.0)
    t.setheading(0)  # Face right
    t.pendown()

    # Angle to turn after each side of the polygon
    exterior_turn = 360.0 / sides

    # To Draw each side of the polygon
    for _ in range(sides):
        inward_koch_edge(t, side_length, depth)
        t.left(exterior_turn)

    # To Show everything at once
    screen.update()
    turtle.done()


def main():
    # Asking user for input values
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Basic checks so the program doesn’t break
    if sides < 3:
        raise ValueError("Number of sides must be at least 3.")

    if side_length <= 0:
        raise ValueError("Side length must be positive.")

    if depth < 0:
        raise ValueError("Recursion depth must be 0 or more.")

    # Start drawing here
    draw_recursive_polygon(sides, side_length, depth)


# Run the program
if __name__ == "__main__":
    main()
