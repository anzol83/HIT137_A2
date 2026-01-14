import turtle

def inward_koch_edge(t, length, depth):
    if depth == 0:
        t.forward(length)

def draw_polygon(sides, side_length, depth):
    t = turtle.Turtle()
    for _ in range(sides):
        inward_koch_edge(t, side_length, depth)
        t.left(360 / sides)

def main():
    # Ask for inputs
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))
    depth = int(input("Enter recursion depth: "))

    turtle.Screen()
    draw_polygon(sides, side_length, depth)
    turtle.done()

if __name__ == "__main__":
    main()
