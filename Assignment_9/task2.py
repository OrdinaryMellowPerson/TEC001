def find_keyword(filename, keyword):
    line_numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if keyword in line:
                    line_numbers.append(line_number)
        return line_numbers
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

if __name__ == "__main__":
    keyword_to_find = "Python"
    lines = find_keyword('task2_test.txt', keyword_to_find)
    print(f"Keyword '{keyword_to_find}' found on lines: {lines}")