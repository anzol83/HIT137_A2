import turtle

def inward_koch_edge(t, length, depth):
    # Stop recursion
    if depth == 0:
        t.forward(length)
        return

    # Split line into three parts
    third = length / 3

    inward_koch_edge(t, third, depth - 1)

def draw_polygon(sides, side_length, depth):
    t = turtle.Turtle()
    for _ in range(sides):
        inward_koch_edge(t, side_length, depth)
        t.left(360 / sides)

def main():
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))
    depth = int(input("Enter recursion depth: "))

    turtle.Screen()
    draw_polygon(sides, side_length, depth)
    turtle.done()

if __name__ == "__main__":
    main()
