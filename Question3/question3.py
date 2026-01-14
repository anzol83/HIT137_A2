import turtle

def main():
    # Ask user for polygon details
    sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))

    screen = turtle.Screen()
    t = turtle.Turtle()

    # Draw a regular polygon
    for _ in range(sides):
        t.forward(side_length)
        t.left(360 / sides)

    turtle.done()

if __name__ == "__main__":
    main()
