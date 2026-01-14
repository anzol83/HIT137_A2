import turtle  # Import the turtle graphics module for drawing

def inward_koch_edge(t, length, depth):
    """
    Recursively draws a single edge with an inward Koch-style indentation.

    Parameters:
    t      : turtle object used for drawing
    length : length of the current line segment
    depth  : recursion depth controlling the level of detail
    """

    # Base case: if recursion depth is 0, draw a straight line
    if depth == 0:
        t.forward(length)
        return

    # Divide the current line segment into three equal parts
    third = length / 3

    # Recursively draw the first third of the segment
    inward_koch_edge(t, third, depth - 1)

    # Turn left to start forming the inward equilateral triangle
    t.left(60)
    inward_koch_edge(t, third, depth - 1)

    # Turn right to create the inward indentation
    t.right(120)
    inward_koch_edge(t, third, depth - 1)

    # Turn left again to align with the original direction
    t.left(60)
    inward_koch_edge(t, third, depth - 1)

def draw_polygon(sides, side_length, depth):
    """
    Draws a regular polygon where each edge is modified using recursion.

    Parameters:
    sides       : number of sides of the polygon
    side_length : length of each side of the initial polygon
    depth       : recursion depth for the pattern
    """

    # Create a turtle object for drawing
    t = turtle.Turtle()
    t.speed(0)  # Set maximum drawing speed for faster rendering

    # Draw each side of the polygon
    for _ in range(sides):
        # Draw a recursively modified edge
        inward_koch_edge(t, side_length, depth)

        # Rotate the turtle to draw the next side of the polygon
        t.left(360 / sides)

def main():
    """
    Main function that takes user input and starts the drawing process.
    """

    # Get user inputs
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))
    depth = int(input("Enter recursion depth: "))

    # Setting up the turtle graphics window
    turtle.Screen()

    # Drawing the recursive polygon
    draw_polygon(sides, side_length, depth)

    # This Keeps the window open until the user closes it
    turtle.done()

# Running the program only if this file is executed directly
if __name__ == "__main__":
    main()
