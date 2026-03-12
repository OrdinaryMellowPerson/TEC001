def remove_odd_numbers(number_list):
    even_list = []

    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)

    return even_list

def main():
    original = []

    print("--- EVEN NUMBER FILTER ---")
    while True:
        user_input = input("Enter an integer (or press Enter to stop): ")

        if user_input == "":
            break

        try:
            num = int(user_input)
            original.append(num)
        except ValueError:
            print("Error: Please enter a valid integer!")
    cut_down = remove_odd_numbers(original)

    print("\nOriginal list:", original)
    print("Cut-down list:", cut_down)
main()