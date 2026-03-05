import random
def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x ** 2) + (y ** 2) < 1:
            points_inside_circle += 1

    pi_value = 4 * points_inside_circle / num_points
    return pi_value


def main():
    print("--- PI APPROXIMATION (MONTE CARLO METHOD) ---")

    while True:
        user_input = input("Enter number of random points to generate (or press Enter to quit): ")

        if user_input == "":
            print("Program terminated.")
            break

        try:
            total_points = int(user_input)

            if total_points <= 0:
                print("Please enter a positive integer.")
                continue

            print(f"Calculating... scattering {total_points} points.")
            result = approximate_pi(total_points)

            print(f"Approximate value of Pi: {result}\n")

        except ValueError:
            print("Invalid input! Please enter an integer number.")


if __name__ == "__main__":
    main()