def get_even_numbers(original_list):
    even_list = []
    for num in original_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

my_numbers = [11, 22, 33, 44, 55, 66, 77, 88]
cut_down_list = get_even_numbers(my_numbers)

print(f"OG List: {my_numbers}")
print(f"Sorted one: {cut_down_list}")