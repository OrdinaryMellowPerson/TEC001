def count_lines(filename):
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    count += 1
        return count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0

if __name__ == "__main__":
    result = count_lines('task1_test.txt')
    print(f"Total non-blank lines: {result}")