numbers = []
while True:
    entry = input("Enter a number OR nothing: ")
    if entry == "":
        break

    numbers.append(float(entry))

numbers.sort(reverse=True)
print("\n--- 一，二，三，四，五 ---")
for n in numbers[:5]:
    print(n)