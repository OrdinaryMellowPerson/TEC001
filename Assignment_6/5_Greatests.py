def task_1():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")

    numbers.sort(reverse=True)

    print("The five greatest numbers are:")
    print(numbers[:5])
task_1()