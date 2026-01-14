import turtle

def inward_koch_edge(t, length, depth):
    # Base case: draw straight line
    if depth == 0:
        t.forward(length)

def draw_polygon(sides, side_length):
    t = turtle.Turtle()
    for _ in range(sides):
        inward_koch_edge(t, side_length, 0)
        t.left(360 / sides)

def main():
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))

    turtle.Screen()
    draw_polygon(sides, side_length)
    turtle.done()

if __name__ == "__main__":
    main()
