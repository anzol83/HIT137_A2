import turtle

def main():
    # Ask user for line length
    side_length = float(input("Enter side length: "))

    screen = turtle.Screen()
    t = turtle.Turtle()

    # Draw line using user input
    t.forward(side_length)

    turtle.done()

if __name__ == "__main__":
    main()
