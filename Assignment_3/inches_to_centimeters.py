import sys

while True:
    try:
        inches = float(input("inches ( input (-) to quit ): "))
        if inches < 0:
            print("Blud even put (-) into and broke the whole thing! 😭", file=sys.stderr)
            break

        cm = inches * 2.54
        print(f"{inches} inches = {cm:.2f} cm\n")

    except ValueError:
        print("Error: pls input numbers! ", file=sys.stderr)