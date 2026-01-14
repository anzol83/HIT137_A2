import turtle

def draw_polygon(sides, side_length):
    # Draw polygon using loop
    t = turtle.Turtle()
    for _ in range(sides):
        t.forward(side_length)
        t.left(360 / sides)

def main():
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))

    turtle.Screen()
    draw_polygon(sides, side_length)
    turtle.done()

if __name__ == "__main__":
    main()
