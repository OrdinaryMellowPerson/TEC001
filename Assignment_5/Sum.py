import re

def sum_numbers_in_text(text):
    number_strings = re.findall(r'\d+', text)
    total_sum = 0
    for num_str in number_strings:
        total_sum += int(num_str)

    return total_sum

sample_text = input("mi tom bo kho radio:")
print(f"here u go: {sum_numbers_in_text(sample_text)}")