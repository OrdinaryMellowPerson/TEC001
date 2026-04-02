def calculate_average(filename):
    total_score = 0
    student_count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 2:
                        try:
                            score = float(parts[1])
                            total_score += score
                            student_count += 1
                        except ValueError:
                            print(f"Warning: Invalid score -> {line}")
        if student_count == 0:
            return 0.0
        return total_score / student_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0.0

if __name__ == "__main__":
    avg_score = calculate_average('task3_test.txt')
    print(f"The average score is: {avg_score}")