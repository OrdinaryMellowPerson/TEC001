talents = float(input("Enter talents: ")) #1talent bằng 20pounds
pounds = float(input("Enter pounds: ")) #1pound bằng 32lots
lots = float(input("Enter lots: ")) #1lot bằng 13,33grams


total_lots = (talents * 20 * 32) + (pounds * 32) + lots
total_grams = total_lots * 13.3

kilograms = int(total_grams // 1000)
remaining_grams = (total_grams % 1000)

print("The weight in modern units:")
print(kilograms, "kilograms and", remaining_grams, "grams.")